import './App.css'
import {VocabularyList} from "./components/vocabulary/VocabularyList.jsx";
import {useEffect, useState} from "react";
import {AddWordDialog} from "./components/vocabulary/AddWordDialog.jsx";
import {fetchVocabulary} from "./services/vocabularyService.js";

function App() {

    const VOCABULARY_URL = 'https://c0ouez95i5.execute-api.us-west-2.amazonaws.com/daily-dragon/vocabulary'

    const [items, setItems] = useState([]);

    useEffect(() => {
        fetchVocabulary()
            .then(setItems)
            .catch(err => {
                // Handle error (show message, etc.)
                console.error(err);
            });
    }, []);

    return (
        <>
            <div className="centered">
                <h1>每日龙</h1>
                <AddWordDialog />
                <VocabularyList items={items}/>
            </div>
        </>
    )
}

export default App
