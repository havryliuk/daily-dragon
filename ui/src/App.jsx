import './App.css'
import {VocabularyList} from "./components/vocabulary/VocabularyList.jsx";
import {useEffect, useState} from "react";
import {AddWordDialog} from "./components/vocabulary/AddWordDialog.jsx";

function App() {

    const VOCABULARY_URL = 'https://c0ouez95i5.execute-api.us-west-2.amazonaws.com/daily-dragon/vocabulary'

    const [items, setItems] = useState([]);

    useEffect(() => {
        const username = 'havryliuk';
        const password = 'juswenko';
        const headers = new Headers();
        headers.set('Authorization', 'Basic ' + btoa(username + ':' + password));

        fetch(VOCABULARY_URL, {headers})
            .then(res => res.json())
            .then(data => setItems(Object.keys(data)));
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
