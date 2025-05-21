import {Button, Menu, Portal} from "@chakra-ui/react";
import {useNavigate} from 'react-router-dom';

export function MainMenu() {
    const navigate = useNavigate();

    return (
        <Menu.Root>
            <Menu.Trigger>
                <Button size="sm" variant="outline">
                    🐉
                </Button>
            </Menu.Trigger>
            <Portal>
                <Menu.Positioner>
                    <Menu.Content>
                        <Menu.Item onClick={() => navigate('/')}>Main Page</Menu.Item>
                        <Menu.Item onClick={() => navigate('/vocabulary')}>Vocabulary</Menu.Item>
                    </Menu.Content>
                </Menu.Positioner>
            </Portal>
        </Menu.Root>
    )
}
