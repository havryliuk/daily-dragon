import {CloseButton, HStack, Text} from "@chakra-ui/react";

interface VocabularyItemProps {
    word: string;
    onRemove: (word: string) => void;
}

const VocabularyListItem: React.FC<VocabularyItemProps> = ({word, onRemove}) => (
    <HStack justify="space-between" w="100%">
        <Text>{word}</Text>
        <CloseButton variant="ghost" colorPalette="red" onClick={() => onRemove(word)}/>
    </HStack>
);

export default VocabularyListItem;