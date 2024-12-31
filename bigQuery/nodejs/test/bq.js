import {OptionsBuilder} from "@davidkhala/gcp-format/auth.js";
import {BigQuery} from "../index.js";

export function getInstance() {
    const optionsBuilder = new OptionsBuilder('gcp-data-davidkhala')
    optionsBuilder.apiKey = process.env.API_KEY
    return new BigQuery(optionsBuilder.build())
}