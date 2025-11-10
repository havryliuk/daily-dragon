import {Button, Text} from "@chakra-ui/react";

export default function PracticePage({onReview}) {
    return (
        <>
            <Text>Translate the following sentences into Chinese using the correct translation of the underlined
                word.</Text>
            <Button colorPalette="blue" variant="subtle" onClick={onReview}>Go to Review</Button>
        </>
    )
}
