const VOCABULARY_URL = 'https://c0ouez95i5.execute-api.us-west-2.amazonaws.com/daily-dragon/vocabulary';
const USERNAME = 'havryliuk';
const PASSWORD = '********';
const BASIC_AUTH = 'Basic ' + btoa(USERNAME + ':' + PASSWORD);

export async function fetchVocabulary() {
    const headers = new Headers();
    headers.set('Authorization', BASIC_AUTH);

    const response = await fetch(VOCABULARY_URL, {headers});
    if (!response.ok) {
        throw new Error('Failed to fetch vocabulary');
    }
    const data = await response.json();
    return Object.keys(data);
}

export async function addWord(trimmedWord) {
    return await fetch(VOCABULARY_URL, {
        method: "POST",
        headers: {
            "Authorization": BASIC_AUTH,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({word: trimmedWord}),
    });
}
