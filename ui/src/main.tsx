import React from 'react';
import ReactDOM from 'react-dom/client';
import {ChakraProvider, defaultSystem} from '@chakra-ui/react';
import Layout from './home.tsx';
import './index.css';
import {BrowserRouter} from "react-router";

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <BrowserRouter>
            <ChakraProvider value={defaultSystem}>
                <Layout/>
            </ChakraProvider>
        </BrowserRouter>
    </React.StrictMode>
);
