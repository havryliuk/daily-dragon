import {HStack, Text} from '@chakra-ui/react'
import {MainMenu} from "./MainMenu";

export function Header() {
    return (
        <header>
            <HStack>
                <MainMenu/>
                <Text>每日龍</Text>
            </HStack>
        </header>
    )
}