export function VocabularyList({items}) {
    return (
        <ul class="no-bullets">
            {items.map((item, index) => (
                <li key={index}>
                    <strong>{item}</strong>
                </li>
            ))}
        </ul>
    );
}