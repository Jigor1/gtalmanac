---
name: "gtalmanac-shorts"
description: "Produz os vídeos curtos do canal GTAlmanac (em inglês: GTA 6, GTA 5, Rockstar) — pauta viral, roteiro, narração no ElevenLabs e vídeo vertical no estilo do canal."
---

# GTAlmanac — vídeos curtos (GTA 6 e universo GTA)

Use esta skill sempre que o Igor pedir um vídeo, roteiro, pauta ou ajuste para o GTAlmanac. Ela guarda o contexto do canal, a linha editorial, o estilo visual aprovado e o caminho até o vídeo pronto. O Igor não programa: entregue sempre o MP4 pronto e a capa, nunca comandos para ele rodar.

## O canal
- **Nome:** GTAlmanac (@gtalmanac) = "GT" + "Almanac", aproveitando o "A" de GTA. Na marca, só o "A" fica rosa (GT**A**LMANAC). Em 28/09/2026 o @ estava livre no YouTube e no Instagram; TikTok e X o Igor conferiria.
- **Público:** americano. Tudo em inglês, valores em dólar.
- **Formato:** Shorts, Reels e TikTok de 45 a 65 s, em motion graphics narrados (sem gameplay).
- **Objetivo (desde 05/10/2026): viralizar.** Na fase de crescimento, o alvo são vídeos de milhões de views. Não precisa ser só notícia: curiosidades, histórias, coisas engraçadas, comparações e "do contra" valem.
- **Temas:** GTA 6 é o centro, mas o canal pode desviar para temas satélites: GTA 5 (já validado e muito buscado), jogos antigos da série, Red Dead, a Rockstar (história, bastidores, polêmicas), a Take-Two (dona da Rockstar), atores e criadores ligados aos jogos, preços de jogos e consoles ligados ao GTA 6.
- **Sem fonte na tela e sem checagem rigorosa** (pedido do Igor em 05/10/2026). O rodapé de fontes fica desligado (`FOOT = []`). Rumor, vazamento e notícia não oficial podem entrar; nesse caso, avise no fim do vídeo (ex.: "Heads up: this comes from a leaked memo, not an official announcement."). Mesmo assim, não invente números nem afirme como fato algo que você sabe que é falso: comentário de "fake" derruba o alcance.
- **Perfil de fã:** bio "Fan channel · not affiliated with Rockstar Games". O logo da Rockstar nunca vira marca do canal. Rumores e vazamentos são tema livre (decisão do Igor, 08/10/2026: o objetivo é viralizar com TUDO do mundo GTA). Reporte o vazamento com aviso de rumor no fim. Pode mostrar cenas/gameplay vazados (decisão do Igor, 08/10/2026), mas sempre desfocados/censurados (blur forte + carimbo "CENSORED"/"BLURRED") para gerar curiosidade; nunca nítidos e nunca nudez visível. Sem acesso ao material, use painéis desfocados com arte oficial e texto animado. Nas legendas e na voz, palavras genéricas ("no clothes"/"outfits") em vez de termos explícitos.
- **Lançamento do GTA 6:** 19/11/2026 (PS5 e Xbox Series X|S). Preços: Standard US$ 79,99, Ultimate US$ 99,99.
- Decisões do Igor ficam na memória, nos arquivos /areas/gtalmanac.md e /areas/gta6-radar.md. Leia antes de começar.

## Fluxo que o Igor espera
1. **Pauta.** O Igor manda um tema (muitas vezes "Faz o vídeo do radar: …") ou pede sugestões. Para sugerir, veja o que está viralizando: `vidiq_outliers` (contentType "short", publishedWithin "thisMonth" ou "threeMonths", sort "breakoutScore") e `vidiq_instagram_tiktok_outlier_search`, mais as notícias da semana (WebSearch). Prefira formatos que já provaram milhões e funcionam sem gameplay: histórias narradas, curiosidades, comparações com números, "do contra", bastidores.
2. **Pesquisa rápida** das fontes (WebSearch/WebFetch) para confirmar números, datas e nomes.
3. **Roteiro** em inglês (regras abaixo). Se o Igor mandou fazer o vídeo, siga direto; só peça aprovação quando ele pedir.
4. **Voz** pelo robô narrador do GitHub (seção Voz). O Igor não precisa baixar nada.
5. **Imagens**: liste para o Igor as que melhorariam a edição e, em paralelo, busque você mesmo pelo robô de imagens (seção Imagens). Monte as cenas enquanto isso.
6. **Vídeo** com o kit (seção Pipeline).
7. **Checagem de qualidade e entrega:** página de download (abaixo), com 3 títulos e uma legenda com hashtags. Depois marque o alerta do radar como feito.
8. **Publicação:** quem posta é o Igor.

## Regras de roteiro
- Entre 120 e 170 palavras (45 a 65 s). Estrutura: gancho forte na primeira frase (paradoxo, número chocante, frase "do contra") → contexto → virada ("But here's the twist.") → detalhe ou dado forte → fechamento com pergunta para os comentários ("Would you pay …? Tell me below."). Se for rumor ou vazamento, avise na frase antes da pergunta.
  - Exemplos de gancho: "GTA 6 costs eighty dollars. And somehow, it's cheaper than GTA 5." / "GameStop is charging fifteen hundred dollars for a used PS5 Pro. Thanks, GTA 6."
- Escreva **por extenso** os preços e decimais ("fifty-nine ninety-nine", "fifteen hundred dollars"). "GTA 6" e anos podem ficar em dígitos. Nunca use "$" ou "%" no texto que vai para a voz. Escreva "PS Five Pro" (não "PS5") e "the U.S." para a voz e o alinhamento funcionarem.
- Frases curtas, com uma ideia por frase.
- Salve em `script.txt` exatamente o texto enviado à voz. O alinhamento das legendas depende disso.

## Série "Who saw GTA 6 first" (convidados do preview na Rockstar North, jul/2026)
- Feitos: Davy Jones (1/4), TGG (2/4), El Rubius (3/4). O Igor desistiu do episódio do **Mike ShowSha** (07/10/2026): não proponha.
- Regras do Igor: nada de informação pessoal; nacionalidade; inscritos e views da plataforma mais forte; curiosidades ligadas ao GTA; o que ele revelou; a abertura cita algo exclusivo de cada um; não diga o nome do canal (use "he", "his channel"); corte curiosidades sem relação com GTA.

## Repositório e robôs (GitHub)
A rede do ambiente bloqueia a ElevenLabs, o storage.googleapis.com e a maioria dos sites, mas o GitHub passa. Tudo que precisa de internet passa por robôs (GitHub Actions) no repositório público **Jigor1/gtalmanac**, que também guarda o kit.
- **Anexe e clone:** `add_repo` (owner `Jigor1`, repo `gtalmanac`, access `push`), depois `git clone --depth 1 https://github.com/Jigor1/gtalmanac /home/claude/gtalmanac`. Se a pasta já existir: `git fetch origin main` e `git reset --hard FETCH_HEAD`.
- **Robôs instalados pelo Igor:** `.github/workflows/narrate.yml` (voz; usa o segredo `ELEVENLABS_API_KEY`, só Text to Speech) e `.github/workflows/fetch-images.yml` (imagens; instalado em 07/10/2026 — se ainda não existir, siga sem ele e peça as imagens ao Igor).
- **Nunca instale nem altere workflows por conta própria.** O sistema de segurança bloqueia, e com razão. Quem instala é o Igor, por um link de 1 clique (`https://github.com/Jigor1/gtalmanac/new/main?filename=.github/workflows/<arquivo>.yml&value=<conteúdo url-encoded>`, de preferência com menos de ~6 mil caracteres).
- **O repositório é público:** só entram roteiros, links públicos de imagens e o kit. Nunca coloque links assinados (como os da ElevenLabs), chaves ou tokens: o sistema bloqueia como vazamento de credencial.
- Ferramentas Python do kit (rode-as você mesmo): `kit/tools/narrate.py`, `kit/tools/images.py`, `kit/tools/splice.py`, `kit/tools/make_page.py`. Leia o topo de cada uma para o uso.

## Voz (ElevenLabs)
- **Voz do canal:** "Adam - Dominant, Firm" (premade), voice_id `pNInz6obpgDQGcFmaJgB`, `model_id: eleven_multilingual_v2`. Não confunda com a outra "Adam" da conta (wBXNqKUATyqu0RtYt25i). Uma versão só.
- **Caminho principal:** `python3 /home/claude/gtalmanac/kit/tools/narrate.py <nome> script.txt narration.mp3`. Ele grava `tts/<nome>.json`, faz push e espera o robô devolver `audio/<nome>.mp3` (de 30 s a 1 min). Se der erro, ele mostra o conteúdo de `audio/<nome>.error.txt`.
  - Cada job gasta créditos. Nunca reenvie o mesmo roteiro "para tentar de novo"; leia o erro primeiro. Use um nome novo por episódio (ex.: `ep11`).
  - Essas narrações aparecem no histórico da ElevenLabs, não nos flows.
- **Plano B:** conector do ElevenLabs (`mcp__ElevenLabs__creative_generate_speech`, `generations_count: 1`, depois `creative_get_flow_run_status`). Mande ao Igor o link do flow para ele baixar e anexar o MP3. Nunca repita uma geração para tentar de novo.

## Imagens
- O Igor gosta de receber a lista de imagens que melhorariam a edição (fotos oficiais, capas, produtos, pessoas, prints de matérias). Mande sempre, mesmo quando o robô já buscou algumas.
- **Robô de imagens:** monte `items.json` e rode `python3 /home/claude/gtalmanac/kit/tools/images.py <ep> items.json assets`. Cada item tem `name` e uma fonte:
  - `page`: matéria ou página oficial → baixa a imagem de capa (og:image). É o melhor caminho para notícias: a capa da matéria costuma ser o print, o produto ou a arte certa.
  - `wiki`: título da Wikipedia → foto principal (pessoas, empresas). `lang` opcional.
  - `url`: link direto de imagem (lojas, CDNs oficiais).
  - `commons`: busca no Wikimedia Commons (fotos livres de lojas, lugares, consoles).
  - O relatório mostra o que veio e o que falhou. Para achar links, use WebSearch/WebFetch nas matérias. Arte oficial do GTA 6: `page` https://www.rockstargames.com/VI.
- X, Reddit e gameplay costumam falhar: peça ao Igor.
- Não gere personagens nem cenas do jogo com IA.

## Estilo visual (não mude sem o Igor pedir)
- **Formato:** 1080×1920, 30 fps, H.264 + AAC. A duração é a da narração.
- **Cores:**
  - Fundo em degradê de #07040F para #2A0E3F.
  - Rosa #FF3D8B/#FF4F9A = GTA 6 e destaques.
  - Ciano #22E4D6 = GTA 5, o passado, "novo".
  - Amarelo #FFD23F = números-chave e etiquetas de preço.
  - Vermelho #FF4D6D = carimbos negativos (USED, SOLD OUT, DENIED).
  - Verde #5BE49B = notícia boa.
- **Posição:** GTA 5 sempre à esquerda, GTA 6 à direita.
- **Fontes:** Anton para títulos, carimbos e legendas; Inter de 600 a 900 para números e rótulos. Números grandes em Inter 900 com dígitos tabulares.
- **Fundo animado:** brilhos rosa e ciano que flutuam, sol synthwave listrado discreto, piso de grade, vinheta e scanlines.
- **Topo:** só a pílula "GT[A]LMANAC | TÓPICO" (y≈196), com o tópico em maiúsculas vindo de `TOPIC_HTML`. **Sem barra de progresso** (o Igor pediu para tirar em 05/10/2026).
- **Zonas seguras:**
  - Conteúdo principal entre y 330 e 1190.
  - Legendas em y≈1292 (Anton 96 px, uma linha; rode `node render.js capcheck`).
  - Nada importante abaixo de y≈1500, nem à direita de x≈960 abaixo de y≈900, onde ficam os botões do TikTok e do Reels.
- **Legendas:** blocos de 2 a 4 palavras; a palavra falada ganha fundo rosa; números-chave em amarelo; contorno preto.
- **Animação:** cada elemento entra no instante em que a palavra correspondente é falada (`w(i)`, de `words.json`). Carimbos entram batendo, com a tela tremendo. Um flash leve marca cada troca de cena. Contadores animam até o valor final; nenhum rótulo pode mentir num quadro intermediário (use "$?,???" até o número ser dito, se preciso).
- **Primeiro quadro:** já mostra algo forte (faça os elementos da cena 1 começarem em t < 0).
- **Recursos que funcionaram (veja `kit/examples`):**
  - Etiqueta de preço amarela que sobe de valor junto com uma escada de barras (Ep. 9 e 10).
  - Itens que saem grandes "de dentro da caixa" e encolhem para uma grade com miniatura (Ep. 8).
  - Print real (memorando, manchete) num cartão branco, com marca-texto amarelo animado sobre a frase-chave e carimbo "LEAKED" (Ep. 10).
  - Citação revelada palavra por palavra junto com a voz (Ep. 9).
  - Semáforo, "the flip" (você → loja → comprador com setas e valores), comparação lado a lado com barras.
  - Fechamento com dois botões "I'd pay / No way" ou "Cloud: yes / no".
- **Fotos:** foto pequena (menos de ~400 px) fica melhor num cartão largo do que num círculo grande. Foto de produto com fundo colorido funciona como cartão arredondado. Objeto escuro (caixa preta, console) ganha brilho rosa (`filter: drop-shadow(0 0 46px rgba(255,79,154,.6))`) para não sumir no fundo. Para tirar fundo de cor sólida, recorte por contorno (polígono) em vez do `cutout.py`, que só serve para fundo branco.
- **Capa:** `node render.js cover <t>` num momento em que o gancho está completo (sai sem legenda). Entregue duas opções: uma com foto/arte e outra com o gráfico mais forte.

## Pipeline (kit em Jigor1/gtalmanac/kit)
1. Pasta do episódio (ex.: /home/claude/ep11/assets). Copie `kit/{setup.sh,align.py,captions.py,build.py,render.js,cutout.py,sheet.py,video.html}` e rode `bash setup.sh`.
2. `script.txt` + `narration.mp3` (pelo robô). Imagens em `assets/`.
3. `python3 align.py narration.mp3 script.txt` → `words.json` com índice, tempo e palavra. Palavra fora do dicionário: acrescente a pronúncia ARPAbet em `CUSTOM` (e leve a mudança para `kit/align.py` no repositório).
4. `chunks.txt` (formato no topo de captions.py; `TEXT:n` consome n palavras faladas, ex. `*$1,500:3` para "fifteen hundred dollars", `IN *2024,:3` para "twenty twenty-four") e `python3 captions.py chunks.txt`.
5. Escreva `scenes_html.txt` e `scenes_js.txt` (blocos VIDEO-SPECIFIC com as linhas de marcação; veja `kit/examples`) e rode `python3 /home/claude/gtalmanac/kit/tools/splice.py video.html scenes_html.txt scenes_js.txt`. No JS: `TOPIC_HTML`, `SC` (limites das cenas com `w(i)`), `SLAMS`, `FOOT = []`, funções `s1..sN` e `SCENES`. Use `A(el, t, início, fimDaCena, {back, s0, dy, dx, d, od, fast, rot})`. Cuidado: um filho com `visibility: visible` aparece mesmo com o pai escondido; use `inherit`.
6. `python3 build.py narration.mp3` → `page.html`.
7. Prévia: `node render.js preview 0 5 12 …` e `python3 sheet.py <scratchpad>/sheet.jpg $(ls prev/*.png | sort -t_ -k2 -g)`. Olhe a folha com Read. `node render.js capcheck` e divida os blocos que quebram linha. Corrija sobreposições, vazios longos, sincronia e zonas seguras.
8. Render: `nohup node render.js video narration.mp3 out.mp4 > render.log 2>&1 &` (5 a 8 min; espere em laços de até 9 min). Capas: `node render.js cover <t> capa.png`.
9. Checagem final: `python3 sheet.py <scratchpad>/chk.jpg --video out.mp4 2 9 16 …`. Confira áudio e duração.

## Página de download (o Igor não consegue baixar arquivos direto do app)
- Gere com `python3 /home/claude/gtalmanac/kit/tools/make_page.py page.json <pasta>`, com `{"ep": "11", "label": "…", "dur": "58 s", "slug": "…", "titles": [3 títulos], "caption": "legenda + hashtags"}`. A página tem player, botões "Baixar vídeo", "Baixar capa" e "Capa alternativa" (capability downloads) e a seção "Para postar" com botões "Copiar". Textos em português; títulos e legenda em inglês.
- Coloque na pasta `video.mp4`, `capa.png` e `capa2.png`. Limite de 15 MB por arquivo: se o MP4 passar, recodifique com `ffmpeg -i in.mp4 -c:v libx264 -crf 22 -preset slow -pix_fmt yuv420p -movflags +faststart -c:a copy video.mp4`.
- Publique com a ferramenta Artifact: `file_path` = a página, `root` = a pasta, `files: {"video.mp4": "video.mp4", "capa.png": "capa.png", "capa2.png": "capa2.png"}`, `capabilities: {"downloads": {}}`, `icon: "video"`. A pasta precisa estar dentro do diretório de trabalho atual ou do scratchpad; se não estiver, copie os 4 arquivos para uma pasta no scratchpad antes.

## Checagem antes de entregar
- Os números na tela batem com a narração; nenhum rótulo enganoso nos quadros intermediários dos contadores.
- Nada cortado ou sobreposto; legendas numa linha só; conteúdo fora das zonas de interface.
- Nenhum trecho longo de tela vazia; o primeiro quadro já mostra algo forte.
- Se o vídeo trouxer rumor ou vazamento, o aviso está no fim.

## Radar e produção automática
- Painel com os alertas: https://claude.ai/artifact/EVBpvZYdpSJRtiEqHntH3V (coleção `alerts`, documento `meta/status`). A tarefa agendada "Radar viral GTAlmanac" (trig_01UHru2Z32uYZz3CkqhjbEvQ) varre a cada 2 h.
- **Produção automática (pedido do Igor em 07/10/2026):** quando um alerta tem status "novo", urgency "agora" ou "hoje" e score 80 ou mais, a própria varredura produz o vídeo sozinha (no máximo 1 por varredura e 2 por dia, controlados por `autoDate`/`autoCount` em meta/status). Ela marca o alerta como `auto`, segue esta skill sem perguntar nada, publica a página e grava `status: "pronto"`, `videoPage` e `autoNote`. Se falhar, volta o alerta para "novo" com o motivo em `autoNote`. O Igor revisa antes de postar.
- Status dos alertas: `novo`, `fazendo` (Em produção), `auto` (produzindo sozinho), `pronto` (vídeo pronto), `feito`, `ignorado`. Quando o Igor pede "Faz o vídeo do radar: …", use o gancho e o ângulo do alerta e, depois de entregar, marque `status: "feito"` (ArtifactData `update` com `if_version`).

## Banco de pautas (07/10/2026)
- **Feito:**
  - Ep. 1, "GTA 6 vs GTA 5 price check": inflação pelo CPI-U, set/2013 = 234,149 → ago/2026 = 334,980 (×1,43). US$ 59,99 viram ≈ US$ 86. Dia 1 do GTA 5, US$ 800M (Take-Two, 18/09/2013), viram ≈ US$ 1,14B. Pré-vendas do GTA 6 ≈ 4,6M / ≈ US$ 446M, com ~89% na edição Ultimate (Sensor Tower, fim de ago/2026).
  - Ep. 2, Davy Jones; Ep. 3, TGG; Ep. 4, El Rubius (série "Who saw GTA 6 first").
  - Ep. 5, classificação etária vazada; Ep. 6, Lindsay Lohan vs Rockstar; Ep. 7, GTA 6 no PC pelo Xbox Cloud (a Xbox negou); Ep. 8, caixa de colecionador de US$ 399,99 sem o jogo (vs RDR2 US$ 99,99); Ep. 9, Martin Klima (Warhorse) quer que o GTA 6 normalize jogos de US$ 80; Ep. 10, memorando vazado da GameStop com PS5 Pro usado a US$ 1.399,99/1.499,99 (troca a US$ 800/850; novo US$ 899,99; QSSR no PS5 comum).
- **Ideias com prova de viralização (vidIQ, out/2026):**
  - "Do contra": "GTA 5 did this BETTER than GTA 6" fez 4,9M num canal de 45 mil inscritos.
  - Histórias narradas de GTA 5: "He got banned for following traffic laws in GTA 5" (2M, canal de 3,6 mil); "How Franklin met IShowSpeed" (2M, canal de 2,5 mil).
  - Curiosidades e easter eggs: "Trevor had a futuristic car 20 years ago" (2,3M).
  - Rockstar: "Rockstar tried to fool players in this scene" (2,4M), "Rockstar made a surfing game?!" (1,2M).
  - Tamanho de Leonida e tempo para atravessar o mapa (4,5M no TikTok, 2M no Reels).
  - A história mais longa da série (~80 h no GTA 6, com objetivos opcionais; 1M no TikTok).
- **Outras pautas:**
  - Atores do GTA 5 hoje (Ned Luke, Steven Ogg, Shawn Fonteno; o ator do Trevor esteve em The Walking Dead). Há um lembrete agendado para 10/10.
  - "GTA existe por causa de um bug" (perseguições policiais no GTA 1, 1997; nasceu como "Race'n'Chase" na DMA Design, o estúdio de Lemmings).
  - A Take-Two (dona da Rockstar) também é dona da Zynga, de FarmVille.
  - Edição da LOVE Magazine (05/10/2026): Jason e Lucia querem casa, família e pagar dívidas, não ficar ricos.
  - Efeito Netflix: +436% em pré-vendas no dia do Extended Look (27/08/2026); +606% no PS5 e +127% no Xbox (Sensor Tower).
  - Escada de recordes: GTA 4 fez US$ 310M no dia 1, o GTA 5 fez US$ 800M. E o GTA 6?
  - Mesmo CEO 13 anos depois (Strauss Zelnick).
  - Preço pelo mundo (Índia ₹5.999; confira loja por loja).
  - Contagem regressiva diária até 19/11.
- **Rumores (podem entrar, com aviso no fim):** cópia física só com código de download; 30 fps nos consoles; projeção de 25M de pré-vendas até o lançamento.

## Robô leitor (artigos completos)
`python3 kit/tools/read.py <nome> <url> [<url>...] --out <pasta>` baixa o texto completo (TITLE/DATE/URL/SUMMARY + corpo) pelo GitHub (`read/` → `articles/`, workflow `read-articles.yml`). Use para checar fatos antes de gravar o roteiro; o radar descobre as notícias por WebSearch e lê os artigos por este robô (WebFetch falha em rotinas sem supervisão).

## Aprovação e publicação (regra do Igor, atualizada em 10/10/2026)
- **Vídeos pedidos numa conversa com o Igor:** nenhum é publicado sem a aprovação dele. Entregue a página de download, espere o "aprovado" e só então copie o MP4 e a capa para `publish/`, agende pelo Metricool (createScheduledPost, melhor horário via getBestTimeToPostByNetwork) e confirme com getScheduledPosts. Depois apague os arquivos de `publish/` (o Metricool guarda a própria cópia).
- **Vídeos produzidos pela rotina do radar:** o Igor autorizou, em 10/10/2026, que a rotina agende sozinha, sem aprovação prévia. Ele ainda pode mudar ou cancelar no Metricool.
