import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import {ChakraProvider, defaultSystem} from '@chakra-ui/react';
import App from './App';
import './index.css';
import {BrowserRouter} from "react-router-dom";

ReactDOM.createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <ChakraProvider value={defaultSystem}>
            <App/>
        </ChakraProvider>
    </BrowserRouter>
);