import {Button, CloseButton, Dialog, Input, useDialogContext} from "@chakra-ui/react"
import {useState} from "react";

function AddWordDialogContent({ word, setWord, loading, setLoading }) {
    const dialog = useDialogContext();

    const handleSave = async () => {
        const trimmedWord = word.trim();
        if (!trimmedWord) return;
        setLoading(true);
        try {
            const response = await fetch("/api/words", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ word: trimmedWord }),
            });
            if (response.ok) {
                setWord("");
                dialog.onClose(); // closes dialog!
            } else {
                // handle error
            }
        } catch (err) {
            // handle error
        }
        setLoading(false);
    };

    return (
        <>
            <Dialog.CloseTrigger asChild>
                <CloseButton />
            </Dialog.CloseTrigger>
            <Dialog.Header>
                <Dialog.Title>Add New Word</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
                <Input
                    placeholder="Enter new word"
                    value={word}
                    onChange={e => setWord(e.target.value)}
                />
            </Dialog.Body>
            <Dialog.Footer>
                <Button
                    colorScheme="blue"
                    onClick={handleSave}
                    isDisabled={word.trim() === "" || loading}
                    isLoading={loading}
                >
                    Save
                </Button>
            </Dialog.Footer>
        </>
    );
}

export function AddWordDialog() {
    const [word, setWord] = useState("");
    const [loading, setLoading] = useState(false);

    return (
        <Dialog.Root>
            <Dialog.Trigger asChild>
                <Button title="Add new word">+</Button>
            </Dialog.Trigger>
            <Dialog.Backdrop />
            <Dialog.Positioner>
                <Dialog.Content>
                    <AddWordDialogContent
                        word={word}
                        setWord={setWord}
                        loading={loading}
                        setLoading={setLoading}
                    />
                </Dialog.Content>
            </Dialog.Positioner>
        </Dialog.Root>
    );
}