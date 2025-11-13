export const GET_SENTENCES_PROMPT = "take these words: ${words}, create 5 sentences with them in ${targetLanguage}. " +
    "return the ${targetLanguage} sentences only and enclose the corresponding English word in triangular brackets. " +
    "Return ONLY a JSON array of strings like this: ['Please, pass me that <english_word>.', ... ]"

export const EVALUATE_TRANSLATIONS_PROMPT = "You are a Chinese tutor. Evaluate each user translation for " +
    "use of the target word, correctness and fluency. Return ONLY valid JSON array, each object after example: " +
    "{\n" +
    "  \"originalSentence\": \"我爱你\",\n" +
    "  \"userTranslation\": \"我喜欢你\",\n" +
    "  \"targetWord\": \"爱\" (ài),\n" +
    "  \"wordUsed\": \"喜欢\",\n" +
    "  \"feedback\": \"\",\n" +
    "  \"score\": 5/10\n" +
    "}\n" +
    "\n" +
    "Evaluate:\n"
