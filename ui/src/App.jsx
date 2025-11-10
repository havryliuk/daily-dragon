import './App.css'
import {Route, Routes} from 'react-router-dom'
import {VocabularyList} from "./components/vocabulary/VocabularyList.jsx";
import {useEffect, useState} from "react";
import {AddWordDialog} from "./components/vocabulary/AddWordDialog.jsx";
import {fetchVocabulary} from "./services/vocabularyService.js";
import Practice from "./components/practice/Practice.jsx";
import {Heading, Spinner} from "@chakra-ui/react";

function App() {

    const [items, setItems] = useState([]);
    const [loadingVocabulary, setLoadingVocabulary] = useState(true);

    useEffect(() => {
        fetchVocabulary()
            .then(vocabulary => {
                setItems(vocabulary);
                setLoadingVocabulary(false);
            })
            .catch(err => {
                // Handle error (show message, etc.)
                console.error(err);
            });
    }, []);

    return (
        <>
            <div className="centered">
                <Heading>每日龙</Heading>
                <Routes>
                    <Route path="/vocabulary" element={
                        <>
                            <AddWordDialog/>
                            {
                                loadingVocabulary ? (<Spinner/>) :
                                    (<VocabularyList items={items}/>)
                            }
                        </>
                    }/>
                    <Route path="/practice" element={<Practice/>}/>
                </Routes>
            </div>
        </>
    )
}

export default App
