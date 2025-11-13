import {Box, Button, List, Spinner, Text} from "@chakra-ui/react";
import {getRandomNWords} from "../../services/vocabularyService.js";
import {useState, useEffect} from "react";
import {getPracticeSentences} from "../../services/ai/aiService.js";

export function PracticePage({onReview}) {
    const [gettingSentences, setGettingSentences] = useState(true);
    const [words, setWords] = useState([]);
    const [sentences, setSentences] = useState([]);

    useEffect(() => {
        (async () => {
            const words = await getRandomNWords(5);
            setWords(words);

            const sentencesResult = await getPracticeSentences(words);
            setSentences(sentencesResult);
            setGettingSentences(false);
        })();
    }, []);



    return (<>
        {gettingSentences ? (<>
            <Text>Getting sentences for translation...</Text>
            <Spinner/>
        </>) : (<>
            <Text>Translate the following sentences into Chinese using the correct translation of the underlined
                word.</Text>
            <Box>
                <List.Root>
                    {sentences.map((sentence, index) => (
                        <List.Item key={index}>{sentence}</List.Item>
                    ))}
                </List.Root>
            </Box>
            <Button colorPalette="blue" variant="subtle" onClick={onReview}>Go to Review</Button>
        </>)}
    </>);
}
