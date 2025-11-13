import {Box, Button, Input, List, Spinner, Text} from "@chakra-ui/react";
import {getRandomNWords} from "../../services/vocabularyService.js";
import {useState, useEffect} from "react";
import {getPracticeSentences, submitTranslations} from "../../services/ai/aiService.js";

export function PracticePage({onReview}) {
    const [gettingSentences, setGettingSentences] = useState(true);
    const [words, setWords] = useState([]);
    const [sentences, setSentences] = useState([]);
    const [translations, setTranslations] = useState({});
    const [submitting, setSubmitting] = useState(false);

    useEffect(() => {
        (async () => {
            const words = await getRandomNWords(5);
            setWords(words);

            const sentencesResult = await getPracticeSentences(words);
            setSentences(sentencesResult);
            setTranslations(Array(sentencesResult.length).fill(""));
            setGettingSentences(false);
        })();
    }, []);

    const handleInputChange = (index, value) => {
        setTranslations((prev) => {
            const updated = [...prev];
            updated[index] = value;
            return updated;
        });
    };

    const allFilled = Array.isArray(translations) && translations.every((t) => (t || "").trim() !== "");

    const handleSubmit = async () => {
        if (!allFilled) return;
        setSubmitting(true);
        try {
            const review = await submitTranslations({words, sentences, translations});
            onReview(review);
        } finally {
            setSubmitting(false);
        }
    };

    return (
        <>
            {gettingSentences ? (<>
                <Text>Getting sentences for translation...</Text>
                <Spinner/>
            </>) : (<>
                <Text>Translate the following sentences into Chinese using the correct translation of the underlined
                    word.</Text>
                <Box m="6px">
                    <List.Root as="ol">
                        {sentences.map((sentence, index) => (
                            <>
                                <List.Item key={index}>{sentence}
                                    <Input
                                        value={translations[index]}
                                        onChange={(e) => handleInputChange(index, e.target.value)}
                                    />
                                </List.Item>
                            </>
                        ))}
                    </List.Root>
                </Box>
                <Button colorPalette="blue" variant="subtle" onClick={handleSubmit}
                        disabled={!allFilled || submitting}>Submit</Button>
                {submitting ? (<>
                    <Text>Submitting your translations...</Text>
                    <Spinner/>
                </>) : null}
            </>)
            }
        </>);
}
