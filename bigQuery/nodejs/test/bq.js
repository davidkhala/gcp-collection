import {OptionsBuilder} from "@davidkhala/gcp-format/auth.js";
import {BigQuery} from "../index.js";

export function getInstance() {
    const optionsBuilder = new OptionsBuilder('gcp-data-davidkhala')
    optionsBuilder.credentials = {
        client_email: process.env.CLIENT_EMAIL.trim(),
        private_key: process.env.PRIVATE_KEY.trim(),
    }
    return new BigQuery(optionsBuilder.build())
}