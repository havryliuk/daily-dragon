import React from "react";

export function VocabularyList({items}) {
    return (
        <ul className="no-bullets">
            {items.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    );
}
