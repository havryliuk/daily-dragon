import * as React from 'react';
import {Header} from './Header';
import {MainPage} from "./MainPage";
import {VocabularyPage} from "./VocabularyPage";
import {Route, Routes} from "react-router-dom";

const App = () => (
    <>
        <Header/>
        <MainPage/>
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/vocabulary" element={<VocabularyPage />} />
        </Routes>
    </>
);

export default App;