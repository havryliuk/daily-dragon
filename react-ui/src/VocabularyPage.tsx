import {useEffect, useState} from "react";
import {List, Text} from "@chakra-ui/react";
import React from "react";
import VocabularyListItem from "./VocabularyListItem";

export function VocabularyPage() {
    const [vocabulary, setVocabulary] = useState<string[]>([]);

    useEffect(() => {
        const fetchVocabulary = async () => {
            const response = await fetch('http://localhost:8000/daily-dragon/vocabulary');
            const result = await response.json();
            const words = Object.keys(result)
            setVocabulary(words);
        }
        fetchVocabulary();
    }, []);

    const handleRemove = (wordToRemove: string) => {
        setVocabulary((prevWords) => prevWords.filter((word) => word !== wordToRemove));
    };

    return (
        <main>
            <Text>This is the vocabulary page.</Text>
            <List.Root>
                {vocabulary.map((word) => (
                    <List.Item key={word}>
                        <VocabularyListItem word={word} onRemove={handleRemove} />
                    </List.Item>
                ))}
            </List.Root>
        </main>
    );
}
