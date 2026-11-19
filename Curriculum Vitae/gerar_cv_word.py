#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY  = RGBColor(0x1B, 0x2A, 0x4A)
BLUE  = RGBColor(0x25, 0x63, 0xEB)
TEAL  = RGBColor(0x0D, 0x94, 0x88)
MUTED = RGBColor(0x64, 0x74, 0x8B)
BLACK = RGBColor(0x1E, 0x29, 0x3B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def remove_cell_borders(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBdr = OxmlElement('w:tcBdr')
    for side in ('top','left','bottom','right','insideH','insideV'):
        b = OxmlElement(f'w:{side}')
        b.set(qn('w:val'),   'none')
        b.set(qn('w:sz'),    '0')
        b.set(qn('w:space'), '0')
        b.set(qn('w:color'), 'auto')
        tcBdr.append(b)
    tcPr.append(tcBdr)

def section_heading(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after  = Pt(3)
    run = p.add_run(title.upper())
    run.bold = True
    run.font.size  = Pt(9.5)
    run.font.color.rgb = BLUE
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'),   'single')
    bottom.set(qn('w:sz'),    '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '2563EB')
    pBdr.append(bottom)
    pPr.append(pBdr)

def exp_block(doc, org, period, role):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(0)
    r1 = p.add_run(role)
    r1.bold = True
    r1.font.size  = Pt(10)
    r1.font.color.rgb = NAVY
    r2 = p.add_run(f'    {period}')
    r2.font.size  = Pt(9)
    r2.font.color.rgb = MUTED
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after  = Pt(2)
    r3 = p2.add_run(org)
    r3.bold = True
    r3.font.size  = Pt(9.5)
    r3.font.color.rgb = TEAL

def bullet(doc, text, sb=0, sa=1):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(sb)
    p.paragraph_format.space_after  = Pt(sa)
    p.paragraph_format.left_indent  = Cm(0.5)
    r = p.add_run(text)
    r.font.size  = Pt(9.5)
    r.font.color.rgb = BLACK

def proj_block(doc, name, status, stack, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after  = Pt(1)
    r1 = p.add_run(name)
    r1.bold = True
    r1.font.size  = Pt(10)
    r1.font.color.rgb = NAVY
    if status:
        r2 = p.add_run(f'  ({status})')
        r2.font.size  = Pt(9)
        r2.font.color.rgb = MUTED
    ps = doc.add_paragraph()
    ps.paragraph_format.space_before = Pt(0)
    ps.paragraph_format.space_after  = Pt(2)
    rs = ps.add_run(f'Stack: {stack}')
    rs.font.size  = Pt(8.5)
    rs.italic     = True
    rs.font.color.rgb = BLUE
    for b in bullets:
        bullet(doc, b)

# ═══════════════════════════════════════════════════════════════════════════
doc = Document()

for sec in doc.sections:
    sec.top_margin    = Cm(1.5)
    sec.bottom_margin = Cm(1.5)
    sec.left_margin   = Cm(2.0)
    sec.right_margin  = Cm(2.0)

doc.styles['Normal'].font.name = 'Calibri'
doc.styles['Normal'].font.size = Pt(10)

# ── CABEÇALHO ──────────────────────────────────────────────────────────────
tbl = doc.add_table(rows=1, cols=1)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.style = 'Table Grid'
cell = tbl.rows[0].cells[0]
set_cell_bg(cell, '1B2A4A')
remove_cell_borders(cell)

def hdr_para(cell, text, size, color, bold=False, sb=0, sa=2):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(sb)
    p.paragraph_format.space_after  = Pt(sa)
    r = p.add_run(text)
    r.bold = bold
    r.font.size  = Pt(size)
    r.font.color.rgb = color
    r.font.name  = 'Calibri'
    return p

cell.paragraphs[0].clear()
p0 = cell.paragraphs[0]
p0.paragraph_format.space_before = Pt(10)
p0.paragraph_format.space_after  = Pt(2)
r0 = p0.add_run('Ercílio Teixeira Júlio')
r0.bold = True; r0.font.size = Pt(22); r0.font.color.rgb = WHITE; r0.font.name = 'Calibri'

hdr_para(cell, 'Engenheiro de Software Full Stack | DevOps | COO da SOMATEC', 11, RGBColor(0x93,0xC5,0xFD), sa=4)
hdr_para(cell,
    'Luanda, Angola  ·  +244 973 087 388  ·  erciliociu@gmail.com  ·  '
    'linkedin.com/in/erciliojulio  ·  github.com/ErCiLio2',
    9, RGBColor(0xCB,0xD5,0xE1), sa=10)

# ── PERFIL PROFISSIONAL ────────────────────────────────────────────────────
section_heading(doc, 'Perfil Profissional')
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(2)
p.paragraph_format.space_after  = Pt(6)
r = p.add_run(
    'Engenheiro de Software Full Stack e DevOps, COO da SOMATEC. Desenvolve plataformas SaaS, fintech e ERP '
    'para o mercado angolano, da infraestrutura à produção, com foco em arquitecturas multi-tenant, segurança '
    'e conformidade legal. Técnico de TI desde 2018 e engenheiro de software profissional desde 2023, combina '
    'desenvolvimento, operação de sistemas e suporte de infraestrutura. Estudante da 42 Luanda, com base em '
    'programação de sistemas, redes e C/C++.'
)
r.font.size  = Pt(10)
r.font.color.rgb = BLACK

# ── COMPETÊNCIAS TÉCNICAS ──────────────────────────────────────────────────
section_heading(doc, 'Competências Técnicas')

skills = [
    ('Linguagens',       'TypeScript, JavaScript, Python, Go, PHP, Java, C, C++, SQL, Bash'),
    ('Back-end',         'NestJS, Node.js, Fastify, Django, FastAPI, Laravel, Gin, REST, OpenAPI, microserviços, Kafka, Celery'),
    ('Front-end',        'React 19, Next.js, SvelteKit, Vite, Tailwind CSS, PWA, offline-first, acessibilidade WCAG 2.2'),
    ('Mobile e desktop', 'Flutter, React Native (Expo), Electron, Tauri'),
    ('Bases de dados',   'PostgreSQL, MySQL, MongoDB, SQLite, Redis, PgBouncer, MinIO/S3; Prisma, TypeORM, Drizzle, SQLAlchemy'),
    ('DevOps',           'Docker, GitHub Actions (CI/CD), Nginx, Traefik, Cloudflare, Dokploy, VPS, Sentry'),
    ('Testes',           'pytest, Jest, Vitest, Playwright'),
    ('Segurança',        'AES-256-GCM, HMAC-SHA256, JWT, RBAC, OTP, anti-replay, idempotência, auditorias'),
    ('Suporte de TI',    'Parque informático, hardware, sistemas operativos, impressoras, redes TCP/IP, Linux, AnyDesk, Microsoft Office, Primavera'),
]

tsk = doc.add_table(rows=len(skills), cols=2)
tsk.style = 'Table Grid'
for i, (area, comp) in enumerate(skills):
    row = tsk.rows[i]
    c0, c1 = row.cells[0], row.cells[1]
    set_cell_bg(c0, 'EFF6FF')
    for c in (c0, c1):
        for pp in c.paragraphs:
            pp.paragraph_format.space_before = Pt(2)
            pp.paragraph_format.space_after  = Pt(2)
    p0 = c0.paragraphs[0]; p0.clear()
    r0 = p0.add_run(area)
    r0.bold = True; r0.font.size = Pt(9); r0.font.color.rgb = NAVY
    p1 = c1.paragraphs[0]; p1.clear()
    r1 = p1.add_run(comp)
    r1.font.size = Pt(9); r1.font.color.rgb = BLACK
tsk.columns[0].width = Cm(3.8)
tsk.columns[1].width = Cm(13.0)

# ── EXPERIÊNCIA PROFISSIONAL ───────────────────────────────────────────────
section_heading(doc, 'Experiência Profissional')

exp_block(doc, 'SOMATEC — Software Marketing e Tecnologia, Luanda', '01/2023 – Presente', 'COO — Director de Operações')
bullet(doc, 'Lidera a área técnica e operacional de produtos SaaS, fintech e ERP para o mercado angolano.')
bullet(doc, 'Coordena equipas de desenvolvimento, define a arquitectura dos sistemas e elabora propostas técnicas e contratos.')
bullet(doc, 'Participou em consórcio para proposta de cibersegurança OT/SCADA e resposta a incidentes (CSIRT/CERT) no sector energético.')

exp_block(doc, 'ChimGam, Luanda', '2024 – Presente', 'QA Engineer · Tech Leader')
bullet(doc, 'Responsável por qualidade técnica e liderança de processo no FlyPort — SaaS B2B para agências de viagens integrado com GDS Travelport.')
bullet(doc, '+5 700 testes pytest em CI paralelo; OpenAPI 3.1 gerado do código; Django-Q com 9 tarefas activas em produção.')

exp_block(doc, 'AS Consulting & Investments, Luanda', '03/2023 – 01/2026', 'Técnico Sénior de TI, Desenvolvedor Full Stack e DevOps')
bullet(doc, 'Responsável por todo o parque informático da empresa: hardware, sistemas operativos, software, impressoras e redes.')
bullet(doc, 'Prestou suporte técnico presencial e remoto (AnyDesk) e resolveu ocorrências de TI de todos os utilizadores.')
bullet(doc, 'Desenvolveu software e implantou e manteve os sistemas da empresa em produção.')

exp_block(doc, 'Júlios AN — Comércio Geral e Transportes, Lda, Luanda (em simultâneo)', '2024 – 2026', 'Técnico Sénior de TI, Desenvolvedor Full Stack e DevOps')
bullet(doc, 'Exerceu as mesmas funções: suporte técnico, gestão da infraestrutura, desenvolvimento de software e operação de sistemas em produção.')

exp_block(doc, 'Grupo ZonaLink, Luanda', '07/2024 – 09/2024', 'Desenvolvedor de Software')
bullet(doc, 'Desenvolveu aplicações web em PHP e Laravel.')

exp_block(doc, 'Clientes particulares e empresas, Luanda', '2018 – 2023', 'Técnico de TI (Freelance)')
bullet(doc, 'Instalou, configurou e manteve hardware, sistemas operativos e redes; prestou consultoria técnica.')

# ── PROJECTOS ──────────────────────────────────────────────────────────────
section_heading(doc, 'Projectos')

proj_block(doc,
    'Troco Seguro — pagamentos e mobilidade', 'SOMATEC · Em produção',
    'NestJS 11, React, PostgreSQL, Redis, MinIO, Firebase, WhatsApp Cloud API, Docker',
    [
        'Cerca de 180 endpoints REST; pagamentos por QR code com anti-replay duplo; depósitos Multicaixa com webhooks HMAC-SHA256.',
        'KYC pelo Bilhete de Identidade, encriptação AES-256-GCM, locks pessimistas; testes Jest e Playwright E2E em CI.',
    ])

proj_block(doc,
    'FlyPort — SaaS B2B para agências de viagens', 'flyport.tech · Em produção · ChimGam',
    'Django 6, React 19, PostgreSQL, Redis, Travelport GDS, Fabric.js, Docker, Nginx, Cloudflare',
    [
        'Integração GDS Travelport; geração de bilhetes PDF com branding via editor Fabric.js; modelo Trial/Starter/Pro.',
        'Cerca de 5 700 testes pytest; CI/CD com 8 fatias paralelas; migração progressiva Django → SPA React 19.',
    ])

proj_block(doc,
    'Eduka — plataforma de explicações online', 'SOMATEC',
    'Fastify 5, Prisma, PostgreSQL 16, PgBouncer, SvelteKit, Flutter, Redis, MinIO',
    [
        'Arquitectura modular com bus de eventos interno e contrato OpenAPI gerado do código.',
        'Módulos com fronteiras ESLint; segurança reforçada para menores e documentos sensíveis.',
    ])

proj_block(doc,
    'FIP — Financial Intelligence Platform', 'SOMATEC',
    'FastAPI, Celery, Alembic, SvelteKit 2, Svelte 5, PostgreSQL, Redis, MinIO',
    [
        'Inteligência financeira com tarefas assíncronas Celery e dashboard SvelteKit totalmente desacoplado.',
    ])

proj_block(doc,
    'MESA Platform — ERP SaaS multi-tenant', 'SOMATEC · Em produção',
    'NestJS, SvelteKit, PostgreSQL, Redis, Prisma, Docker',
    [
        'ERP para farmácia, hotelaria, educação, restauração e retalho, com flavors visuais e módulos por sector.',
        'Isolamento por schema PostgreSQL por tenant; sistema de flavors sem fork de código.',
    ])

proj_block(doc,
    'WOL Commerce / WOL Loja', 'SOMATEC · Em produção',
    'TypeScript, NestJS, React, MinIO, PostgreSQL',
    [
        'Plataforma B2B e live commerce em produção; módulo de analytics construído de raiz.',
        'Gestão centralizada de media em MinIO; dashboard de vendas e inventário.',
    ])

proj_block(doc,
    'IMS / AprenderAO — plataforma de ensino online', 'SOMATEC',
    'Next.js 16, HeroUI, jsPDF, Playwright',
    [
        'Plataforma de ensino online com geração de PDFs e testes Playwright E2E.',
    ])

# Outros
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(5)
p.paragraph_format.space_after  = Pt(2)
rb = p.add_run('Outros:  ')
rb.bold = True; rb.font.size = Pt(9.5); rb.font.color.rgb = NAVY
rt = p.add_run(
    'SeaOPEX (NestJS, Next.js — ship chandling) · '
    'SaaS de Farmácia (NestJS, Kafka, Electron — offline-first) · '
    'Go API (Gin, QUIC/HTTP3, PostgreSQL + MongoDB)'
)
rt.font.size = Pt(9.5); rt.font.color.rgb = BLACK

# ── FORMAÇÃO ───────────────────────────────────────────────────────────────
section_heading(doc, 'Formação')

exp_block(doc, '42 Luanda (ISPTEC), Talatona', '09/2024 – Presente', 'Engenharia de Software — 42 Luanda')
bullet(doc, 'Em curso: nível 5.13 de 21; tronco comum 57% concluído. Aprendizagem entre pares, baseada em projectos.')
bullet(doc, 'Projectos validados: Born2beroot · NetPractice · minishell · Philosophers · cub3D · push_swap · Libft · fract-ol · get_next_line · ft_printf · minitalk · CPP Módulos 00–04 · Exam Rank 02, 03, 04.')

exp_block(doc, 'IPAS Zango Zero', '2021 – 2025', 'Técnico Médio em Informática de Gestão')

# ── COMPETÊNCIAS CERTIFICADAS PELA 42 LUANDA ──────────────────────────────
section_heading(doc, 'Competências Certificadas pela 42 Luanda')

comp42 = [
    ('Rede e administração de sistemas',
     'Endereços IP, sub-redes, routing, redes locais; instalação de Linux, segurança, utilizadores e armazenamento; e-mail, DNS e servidor web.'),
    ('Programação de sistemas',
     'Chamadas de sistema Unix, sistemas de ficheiros, criação e gestão de processos, pipes e sinais, ioctl, sockets TCP/UDP, resolução DNS.'),
    ('Programação imperativa (C)',
     'Sintaxe, recursividade, estruturas, alocação e libertação de memória, listas ligadas, árvores, biblioteca padrão de C.'),
    ('Programação orientada a objectos (C++)',
     'Classes, namespaces, construtores/destrutores, herança, abstracção, sobrecarga, templates, biblioteca padrão de C++.'),
    ('Algoritmos e IA',
     'Pesquisa, ordenação, inserção, eliminação e balanceamento em arrays, listas ligadas e árvores; máquinas de estados; gestão assíncrona.'),
    ('Gráficos',
     'Manipulação de imagens RGB, desenho, gestão de janelas, eventos de teclado/rato, callbacks e ciclo de eventos.'),
    ('Web',
     'Arquitectura cliente-servidor, HTTP, HTML, CSS, JavaScript, MVC, sessões, autenticação, cookies, back-office, UX e design.'),
    ('Rigor',
     'Cumprimento de requisitos técnicos e administrativos; processos de teste extensos para eliminação de falhas.'),
    ('Trabalho em grupo',
     'Colaboração, gestão de grupos, avaliação entre pares e gestão de conflitos.'),
]

t42 = doc.add_table(rows=len(comp42), cols=2)
t42.style = 'Table Grid'
for i, (area, desc) in enumerate(comp42):
    row = t42.rows[i]
    c0, c1 = row.cells[0], row.cells[1]
    set_cell_bg(c0, 'F0F9FF')
    for c in (c0, c1):
        for pp in c.paragraphs:
            pp.paragraph_format.space_before = Pt(2)
            pp.paragraph_format.space_after  = Pt(2)
    p0 = c0.paragraphs[0]; p0.clear()
    r0 = p0.add_run(area)
    r0.bold = True; r0.font.size = Pt(9); r0.font.color.rgb = TEAL
    p1 = c1.paragraphs[0]; p1.clear()
    r1 = p1.add_run(desc)
    r1.font.size = Pt(9); r1.font.color.rgb = BLACK
t42.columns[0].width = Cm(4.5)
t42.columns[1].width = Cm(12.3)

# ── CERTIFICAÇÕES ──────────────────────────────────────────────────────────
section_heading(doc, 'Certificações')
for c in [
    'Administração de Sistemas Linux — Udemy',
    'Hardware e Software; Informática na Óptica do Utilizador — Centro de Formação Profissional Nelpalma',
    'Programação Web — MundoTec (mundotec.ao)',
    'Next.js App Router Fundamentals; React Foundations for Next.js',
    'LinkedIn para Busca de Oportunidades',
]:
    bullet(doc, c)

# ── EVENTOS ────────────────────────────────────────────────────────────────
section_heading(doc, 'Eventos e Participações')
bullet(doc, 'Unitel Startup Summit — by Unitel, 16–18 Mai 2024  ·  SOMATEC')
bullet(doc, 'Hackathon Academia BAI, 31 Ago 2024  ·  SOMATEC')

# ── IDIOMAS ────────────────────────────────────────────────────────────────
section_heading(doc, 'Idiomas')
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(2)
p.paragraph_format.space_after  = Pt(6)
for part in [('Português', 'nativo'), ('Inglês', 'elementar')]:
    rb = p.add_run(part[0])
    rb.bold = True; rb.font.size = Pt(10); rb.font.color.rgb = BLACK
    rt = p.add_run(f': {part[1]}    ')
    rt.font.size = Pt(10); rt.font.color.rgb = BLACK

out = '/sgoinfre/eteixeir/works/extras/Curriculum Vitae/Ercilio_Julio_CV_2026.docx'
doc.save(out)
print(f'Guardado: {out}')
