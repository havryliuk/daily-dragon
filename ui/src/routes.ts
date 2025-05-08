import {index, route, RouteConfig} from "@react-router/dev/routes";
import Layout from "./home.tsx";

export default [
    route("/", Layout, [
        index("./home.tsx"),
        route("vocabulary", "./pages/vocabulary.tsx")
    ])
] satisfies RouteConfig;
