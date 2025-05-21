import {Flex, Text} from '@chakra-ui/react'
import {MainMenu} from "./MainMenu";

export function Header() {
    return (
        <Flex>
            <Flex>
                <MainMenu/>
                <Text>每日龍</Text>
            </Flex>
        </Flex>
    )
}