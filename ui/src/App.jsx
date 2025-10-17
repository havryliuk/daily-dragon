import './App.css'
import {VocabularyList} from "./components/vocabulary/VocabularyList.jsx";

function App() {

    const items = ["龙", "凤", "虎", "龟", "麒麟"];

    return (
        <>
            <h1>每日龙</h1>
            <VocabularyList items={items}/>
        </>
    )
}

export default App
