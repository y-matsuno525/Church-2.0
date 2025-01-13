# Church2.0(ごちゃごちゃしてきたので作り直しています→https://github.com/y-matsuno525/Church-3.0)
http://13.231.112.58:8000/menu/
（AWS無料枠ギリギリのため現在停止中）

デモ動画
https://youtu.be/ggfkW9GFSes?si=enlyv8lhV14jd4YQ
  
## 概要
- **Church2.0** は、カトリックやプロテスタントなど、既存の教会には属さない独立したプラットフォームで、教会に属さないクリスチャン同士をつなぐことを目的としています。
---

## 機能一覧
- **聖書閲覧機能**: アプリ内で聖書を読むことが可能。
- **生成AIによる教義生成**: 掲示板投稿内容と論文から生成AIが教義を生成。(今はopenaiAPIを使っているが、いずれtranformersでやりたい)
- **ユーザー登録とログイン**: 各ユーザーが個別のアカウントでアプリを利用可能。(論文投稿や論文へのスターなど一部機能はログインユーザー限定)
- **聖句ごとの掲示板**: 聖書の各聖句ごとにディスカッションを行える掲示板機能。
- **投稿の可視化**: Wordcloudを用いて掲示板投稿内容を可視化。
- **論文投稿機能**: 教義や神学に関する論文を投稿でき、Markdown形式で執筆可能。
- **グッズストア**: キリスト教関連のグッズを販売。クレジットカード決済に対応。(stripeによるテスト決済は可能になったが、本番環境では念のため停止中)

---

## カスタムコマンド
- **register**: 獲得スターが一定以上のpreprintをjournalへ掲載
- **visualization**: wordcloudで、掲示板の書き込みを可視化するための画像を生成
---

## 構想中の機能
- **フリーマーケット機能**: ユーザー同士で商品を売買可能なフリーマーケット。
- **サイト内通貨**: クレジット決済に代わる独自のデジタル通貨の導入。

---

## 使用技術
- **言語**: Python 3.13.0
- **フレームワーク**: Django
- **データベース**:
  - 開発環境: SQLite
  - 本番環境: PostgreSQL（予定）
- **デプロイ**: AWS
- **クレジットカード決済**: Stripe(停止中)

---

## セットアップ手順

### 必要要件
- Python 3.10以上
- Git

### インストール手順
1. リポジトリをクローン
   ```bash
   git clone https://github.com/username/church2.0.git
   cd church2.0


# Church2.0

## Overview
**Church2.0** is a new type of online Christian community inspired by Hiroki Azuma's *General Will 2.0* and Kojin Karatani's *Modes of Exchange and Power*.  
This platform is independent of existing churches, such as Catholic and Protestant denominations, and aims to connect Christians who do not belong to any specific church.

---

## Features
- **Bible Reading**: Users can read the Bible within the app.
- **User Registration and Login**: Secure user accounts for personalized access.
- **Verse-Specific Discussion Boards**: Boards dedicated to discussions based on specific Bible verses.
- **Post Visualization**: Wordcloud visualization of discussion board posts.
- **Academic Article Submission**: Submit articles on theology and doctrines with Markdown support.
- **Goods Store**: Online store offering Christian-related merchandise with credit card payment support.

---

## Planned Features
- **AI-Generated Summaries**: Summarization of discussion board content using AI.
- **Free Marketplace**: A feature allowing users to trade goods within the platform.
- **In-App Currency**: A digital currency to replace traditional credit card payments.

---

## Technologies Used
- **Programming Language**: Python 3.13.0
- **Framework**: Django
- **Database**:
  - Development: SQLite
  - Production: PostgreSQL (planned)
- **Deployment**: AWS

---

## Setup Instructions

### Requirements
- Python >= 3.10
- Git

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/church2.0.git
   cd church2.0
