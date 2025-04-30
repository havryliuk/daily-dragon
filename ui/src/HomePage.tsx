import {Box, Button, Flex, Heading, Menu, Portal} from '@chakra-ui/react';

function HomePage() {
    return (
        <Box position="fixed" top="0" left="0" width="100%">
            <Flex justify="center">
                <Box p={4}>
                    <Menu.Root>
                        <Menu.Trigger asChild>
                            <Button variant="ghost" boxSize="10">
                                🐉
                            </Button>
                        </Menu.Trigger>
                        <Portal>
                            <Menu.Positioner>
                                <Menu.Content>
                                    <Menu.Item value="home">
                                        Home
                                    </Menu.Item>
                                    <Menu.Item value="vocabulary">
                                        Vocabulary
                                    </Menu.Item>
                                </Menu.Content>
                            </Menu.Positioner>
                        </Portal>
                    </Menu.Root>
                </Box>
                <Box p={4}>
                    <Heading>每日龙</Heading>
                </Box>
            </Flex>
        </Box>
    );
}

export default HomePage;
