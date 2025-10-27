import {Dialog, Input} from "@chakra-ui/react"

export function AddWordDialog() {
    return (
        <>
            <Dialog.Root>
                <Dialog.Trigger />
                <Dialog.Backdrop />
                <Dialog.Positioner>
                    <Dialog.Content>
                        <Dialog.CloseTrigger />
                        <Dialog.Header>
                            <Dialog.Title>Add New Word</Dialog.Title>
                        </Dialog.Header>
                        <Dialog.Body>
                            <Input placeholder="Enter new word" />
                        </Dialog.Body>
                        <Dialog.Footer />
                    </Dialog.Content>
                </Dialog.Positioner>
            </Dialog.Root>
        </>
    )
}