import {Box, Button, Heading, Menu, Portal} from '@chakra-ui/react';

function HomePage() {
  return (
    <Box p={4}>
      <Heading>每日龙</Heading>
        <Menu.Root>
            <Menu.Trigger asChild>
                <Button variant="outline" size="sm">
                    Menu
                </Button>
            </Menu.Trigger>
            <Portal>
                <Menu.Positioner>
                    <Menu.Content>
                        <Menu.Item value="new-txt-a">
                            Home
                        </Menu.Item>
                        <Menu.Item value="new-file-a">
                            Vocabulary
                        </Menu.Item>
                    </Menu.Content>
                </Menu.Positioner>
            </Portal>
        </Menu.Root>
    </Box>
  );
}

export default HomePage;
