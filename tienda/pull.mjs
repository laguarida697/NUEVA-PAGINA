// Uso: node pull.mjs archivo1 archivo2 ...  (baja archivos del tema de trabajo a ./tema)
import { execFileSync } from "node:child_process";
import fs from "node:fs"; import path from "node:path";
const THEME = "gid://shopify/OnlineStoreTheme/167161987211", STORE = "qf1mmk-ew.myshopify.com";
const names = process.argv.slice(2);
const q = `query($id: ID!, $n: [String!]!) { theme(id:$id){ files(filenames:$n, first:250){ nodes{ filename body{ ... on OnlineStoreThemeFileBodyText{ content } } } } } }`;
fs.writeFileSync("/tmp/q-pull.graphql", q);
const out = execFileSync("shopify", ["store","execute","--store",STORE,"--query-file","/tmp/q-pull.graphql","--variables",JSON.stringify({id:THEME,n:names}),"--json"],{encoding:"utf8",maxBuffer:1e9});
const json = JSON.parse(out.slice(out.indexOf("{")));
for (const f of json.theme.files.nodes) {
  const p = path.join("tema", f.filename); fs.mkdirSync(path.dirname(p),{recursive:true});
  fs.writeFileSync(p, f.body?.content ?? ""); console.log("OK", f.filename);
}
