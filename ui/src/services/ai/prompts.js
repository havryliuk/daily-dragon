export const GET_SENTENCES_PROMPT = "take these words: ${words}, create 5 sentences with them in ${targetLanguage}. " +
    "return the ${targetLanguage} sentences only and enclose the corresponding English word in triangular brackets. " +
    "Return ONLY a JSON array of strings like this: ['Please, pass me that <english_word>.', ... ]"
