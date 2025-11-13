import {Box} from "@chakra-ui/react";
import {useState} from "react";
import WelcomePage from "./WelcomePage.jsx";
import {PracticePage} from "./PracticePage.jsx";
import ReviewPage from "./ReviewPage.jsx";

const STATES = {
    WELCOME: 'WELCOME',
    IN_PROGRESS: 'IN_PROGRESS',
    REVIEW: 'REVIEW'
}

export default function Practice() {
    const [state, setState] = useState(STATES.WELCOME);

    const startPractice = () => setState(STATES.IN_PROGRESS);
    const goToReview = () => setState(STATES.REVIEW);
    const finishPractice = () => setState(STATES.WELCOME);

    return <Box>
        {state === STATES.WELCOME && <WelcomePage onStart={startPractice} />}
        {state === STATES.IN_PROGRESS && <PracticePage onReview={goToReview} />}
        {state === STATES.REVIEW && <ReviewPage onFinish={finishPractice} />}
    </Box>
}
