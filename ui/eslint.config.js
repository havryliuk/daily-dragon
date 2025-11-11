import globals from "globals";
import react from "eslint-plugin-react";
import {defineConfig} from "eslint/config";

export default defineConfig([{
    files: ["**/*.{js,jsx}"],
    plugins: {
        react
    },
    languageOptions: {
        globals: globals.browser,
        parserOptions: {
            ecmaVersion: "latest",
            ecmaFeatures: {jsx: true},
            sourceType: "module"
        }
    },
    ignores: [
        "node_modules/**",
        ".vite/**"
    ],
    rules: {
        "react/react-in-jsx-scope": "off"
    }
}])
;
