import {Button, Text} from "@chakra-ui/react";

export default ({onFinish}) => (
    <>
        <Text>This is the ReviewPage component.</Text>
        <Button colorPalette="blue" variant="subtle" onClick={onFinish}>Finish Practice</Button>
    </>
)
