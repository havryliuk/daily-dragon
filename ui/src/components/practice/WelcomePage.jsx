import {Button, Text} from "@chakra-ui/react";

export default ({onStart}) => (
    <>
        <Text>This is the Practice component.</Text>
        <Button colorPalette="blue" variant="subtle" onClick={onStart}>Start</Button>
    </>
)
