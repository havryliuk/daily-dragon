import React from "react";
import {render, screen} from "@testing-library/react";
import {VocabularyList} from "../../../components/vocabulary/VocabularyList.jsx";

test("renders all words in the list", () => {
    render(<VocabularyList items={["你好", "世界"]}/>);
    expect(screen.getByText("你好")).toBeInTheDocument();
    expect(screen.getByText("世界")).toBeInTheDocument();
});
