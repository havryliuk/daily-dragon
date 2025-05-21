import {useEffect, useState} from "react";
import {List, Text} from "@chakra-ui/react";
import React from "react";

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

    return (
        <>
            <Text>This is the vocabulary page.</Text>
            <List.Root>
                {vocabulary.map((word, index) => (
                    <List.Item key={index}>
                        <Text>{word}</Text>
                    </List.Item>
                ))}
            </List.Root>
        </>
    );
}
