import {Button, Text} from "@chakra-ui/react";

export default ({onStart}) => (
    <>
        <Text>From here you can start practicing translating Chinese sentences</Text>
        <Button colorPalette="blue" variant="subtle" onClick={onStart}>Start</Button>
    </>
)
