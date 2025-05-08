import {Box, Button, Flex, Heading, Menu, Portal} from '@chakra-ui/react';
import {Link, Outlet} from "react-router";

function Layout() {
    return (
        <>
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
                                        <Menu.Item asChild value="home">
                                            <Link to="/">Home</Link>
                                        </Menu.Item>
                                        <Menu.Item asChild value="vocabulary">
                                            <Link to="/vocabulary">
                                                Vocabulary
                                            </Link>
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
            <Box p={4}>
                <Outlet/>
            </Box>
        </>
    );
}

export default Layout;
