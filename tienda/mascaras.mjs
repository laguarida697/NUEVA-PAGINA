import { execFileSync } from "node:child_process"; import fs from "node:fs";
const S="qf1mmk-ew.myshopify.com";
const run=(q,v)=>{ fs.writeFileSync("/tmp/q.graphql",q); const o=execFileSync("shopify",["store","execute","--store",S,"--query-file","/tmp/q.graphql","--variables",JSON.stringify(v),"--allow-mutations","--json"],{encoding:"utf8",maxBuffer:1e9}); return JSON.parse(o.slice(o.indexOf("{"))); };
const COL="gid://shopify/Collection/489961980043";
const items=[
 ["Máscara Calavera Terrorífica","calavera",29900,"Máscara de calavera para tu disfraz de Halloween. Dale un toque aterrador a tu look."],
 ["Máscara Payaso Siniestro","payaso",34900,"Máscara de payaso siniestro, perfecta para fiestas y noches de terror."],
 ["Máscara Vampiro Sangriento","vampiro",32900,"Máscara de vampiro con colmillos y mirada roja para una noche de brujas elegante y siniestra."],
 ["Máscara Zombi Cosido","zombi",27900,"Máscara de zombi con costuras y un ojo desorbitado. Ideal para sustos y fotos."],
 ["Máscara Fantasma Aullador","fantasma",24900,"Máscara de fantasma con boca de grito. Divertida para niños y adultos."],
 ["Máscara Calabaza Maldita","calabaza",26900,"Máscara de calabaza con sonrisa macabra. El clásico de Halloween."],
];
for (const [title,cara,price,desc] of items){
  const c=run(`mutation($p: ProductCreateInput!){ productCreate(product:$p){ product{ id variants(first:1){ nodes{ id } } } userErrors{ field message } } }`,
    {p:{title, descriptionHtml:`<p>${desc}</p><p><strong>Una talla para todos.</strong> Producto de ejemplo: ajusta la descripción y la foto cuando tengas tu proveedor.</p>`, status:"ACTIVE", vendor:"La Guarida del Terror", productType:"Máscaras", tags:["máscara","halloween","cara-"+cara], collectionsToJoin:[COL]}}).productCreate;
  if(c.userErrors.length){console.log("ERR",title,JSON.stringify(c.userErrors));continue;}
  const pid=c.product.id, vid=c.product.variants.nodes[0].id;
  const u=run(`mutation($pid: ID!, $v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$pid, variants:$v){ productVariants{ id price } userErrors{ field message } } }`,
    {pid, v:[{id:vid, price:String(price), inventoryPolicy:"DENY", inventoryItem:{tracked:true}}]}).productVariantsBulkUpdate;
  console.log(title, price, pid, u.userErrors.length?JSON.stringify(u.userErrors):"OK");
}
