import {GET_SENTENCES_PROMPT} from "./prompts.js";

const AI_SERVICE_URL = "https://c0ouez95i5.execute-api.us-west-2.amazonaws.com/daily-dragon/openai";


export async function getPracticeSentences(words) {
    const prompt = GET_SENTENCES_PROMPT
        .replace("${words}", JSON.stringify(words))
        .replace("${targetLanguage}", "English")
        .replace("${targetLanguage}", "English");

    const response = await fetch(AI_SERVICE_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });

    if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
    }

    return await response.json();
}
