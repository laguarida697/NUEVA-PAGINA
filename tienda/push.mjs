// Uso: node push.mjs archivo1 archivo2 ...  (sube archivos de ./tema al tema de trabajo)
import { execFileSync } from "node:child_process";
import fs from "node:fs";
const THEME = "gid://shopify/OnlineStoreTheme/167161987211", STORE = "qf1mmk-ew.myshopify.com";
const names = process.argv.slice(2);
const q = `mutation($id: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert(themeId:$id, files:$files){ upsertedThemeFiles{ filename } userErrors{ filename field message code } } }`;
fs.writeFileSync("/tmp/q-push.graphql", q);
for (let i=0;i<names.length;i+=20){
  const files = names.slice(i,i+20).map(n=>({filename:n, body:{type:"TEXT", value: fs.readFileSync("tema/"+n,"utf8")}}));
  const out = execFileSync("shopify", ["store","execute","--store",STORE,"--query-file","/tmp/q-push.graphql","--variables",JSON.stringify({id:THEME,files}),"--allow-mutations","--json"],{encoding:"utf8",maxBuffer:1e9});
  const r = JSON.parse(out.slice(out.indexOf("{"))).themeFilesUpsert;
  console.log("subidos:", r.upsertedThemeFiles.map(f=>f.filename).join(", "));
  if (r.userErrors.length) { console.log("ERRORES:", JSON.stringify(r.userErrors,null,1)); process.exitCode=1; }
}
