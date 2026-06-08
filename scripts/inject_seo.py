import os
import json
import codecs

messages_dir = os.path.join(os.path.dirname(__file__), '../messages')
en_content = {
    "h2": "What is pure local {brand}?",
    "h2Desc": "Unlike traditional cloud-based PDF tools, {brand} utilizes cutting-edge WebAssembly and HTML5 Canvas technologies to process your files directly within your browser. This means your sensitive documents are never uploaded to any external server. You enjoy 100% privacy, instant processing speeds, and no file size limits imposed by cloud storage.",
    "h3Advantage": "What are the advantages of Client-Side Processing?",
    "h3AdvantageDesc": "By leveraging client-side processing, {brand} eliminates the risk of data breaches during transmission. Operations like PDF merging, splitting, and compression happen locally on your device's CPU and RAM. This architecture not only guarantees absolute data security but also provides a seamless, offline-capable experience once the application is loaded.",
    "h3Features": "Core Features & Capabilities",
    "h3FeaturesDesc": "Experience a comprehensive suite of professional PDF tools at your fingertips. Features include batch processing of multiple files, lossless compression algorithms, intelligent PDF splitting and merging, OCR text extraction, and advanced document security options like password encryption and watermarking—all running locally without requiring internet connectivity."
}

zh_content = {
    "h2": "什么是纯本地的 {brand}？",
    "h2Desc": "与传统的云端 PDF 工具不同，{brand} 利用前沿的 WebAssembly 和 HTML5 Canvas 技术，直接在您的浏览器中处理文件。这意味着您的敏感文档永远不会被上传到任何外部服务器。您将享受 100% 的隐私保护、瞬间的处理速度，以及毫无云端存储限制的文件处理体验。",
    "h3Advantage": "客户端本地处理的优势是什么？",
    "h3AdvantageDesc": "通过采用客户端处理架构，{brand} 彻底消除了数据在网络传输过程中的泄露风险。诸如 PDF 合并、拆分和压缩等所有操作，均完全依赖您当前设备的 CPU 和内存。这种纯本地架构不仅从物理层面保障了绝对的数据安全，还在页面加载完成后提供了无缝的离线可用体验。",
    "h3Features": "核心功能与高级特性",
    "h3FeaturesDesc": "触手可及的专业级 PDF 解决套件。我们的核心功能涵盖多文件批量急速处理、无损压缩算法、智能页面拆分与合并、OCR 光学字符提取，以及密码加密和数字水印等高级文档安全选项——所有这一切都在本地离线运行，不再受制于网络环境。"
}

for filename in os.listdir(messages_dir):
    if filename.endswith('.json') and filename not in ['en.json', 'zh.json']:
        filepath = os.path.join(messages_dir, filename)
        with codecs.open(filepath, 'r', 'utf-8') as f:
            data = json.load(f)
        
        # Don't touch if already has seoArticle
        if 'common' in data and 'seoArticle' not in data['common']:
            if filename.startswith('zh'):
                data['common']['seoArticle'] = zh_content
            else:
                data['common']['seoArticle'] = en_content
            
            with codecs.open(filepath, 'w', 'utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Injected into {filename}")
