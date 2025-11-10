import './App.css'
import {Route, Routes} from 'react-router-dom'
import Practice from "./components/practice/Practice.jsx";
import {Heading} from "@chakra-ui/react";
import VocabularyPage from "./components/vocabulary/VocabularyPage.jsx";

function App() {
    return (
        <>
            <div className="centered">
                <Heading>每日龙</Heading>
                <Routes>
                    <Route path="/vocabulary" element={<VocabularyPage/>}/>
                    <Route path="/practice" element={<Practice/>}/>
                </Routes>
            </div>
        </>
    )
}

export default App
