import {useState} from "react";
import {AddWordDialog} from "./AddWordDialog.jsx";
import {Button} from "@chakra-ui/react";

export function AddWordButton() {
    const [addWordDialogOpen, setAddWordDialogOpen] = useState(false);

    const handleSave = (word) => {
        // Here you would typically send the new word to your backend or update state
        console.log("New word saved:", word);
    }

    return (
        <>
            <Button title="Add new word" onClick={() => setAddWordDialogOpen(true)}>+</Button>
            <AddWordDialog open={addWordDialogOpen} onClose={() => setAddWordDialogOpen(false)} onSave={handleSave}/>
        </>
    )
}
