# GH-600: Developing in Agentic AI Systems - Kapsamlı Çalışma Rehberi (STUDY.md)

Bu rehber, **Microsoft & GitHub Course GH-600T00-A: Developing in Agentic AI Systems** ve **GitHub Certified: Agentic AI Developer** sertifika sınavı müfredatının tamamını kapsayan detaylı ve yapılandırılmış özet çalışma dokümanıdır.

---

## 📌 İÇİNDEKİLER

1. [Bölüm 1: Agentic AI Temelleri ve GitHub Ekosistemi](#bölüm-1-agentic-ai-temelleri-ve-github-ekosistemi)
   - Asistan (Assistant) vs. Ajan (Agent) Ayrımı
   - Plan → Act → Evaluate Yaşam Döngüsü
   - GitHub: System of Record ve Control Plane
   - Sorumluluk Modeli ve Katılımcı Modeli (Contributor Model)
   - Temel Anti-Pattern'ler ve Riskler
2. [Bölüm 2: Ajan Mimarisi ve SDLC Entegrasyonu](#bölüm-2-ajan-mimarisi-ve-sdlc-entegrasyonu)
   - SDLC Aşamalarına Ajan Sorumluluklarının Eşlenmesi
   - Görev Sözleşmesi (Task Contract): Girdiler, Çıktılar, Başarı Kriterleri
   - Plan-First vs. Plan + Execution Modelleri
   - Pull Request Tabanlı Yönetim ve Şablonlar
   - GitHub Actions İş Akışı Mimarisi ($GITHUB_OUTPUT, Contexts, Event Gating)
   - Güvenlik Sınırları ve Kanca (Hook) Mekanizmaları
3. [Bölüm 3: Tooling, MCP ve Yürütme Ortamları](#bölüm-3-tooling-mcp-ve-yürütme-ortamları)
   - Model Context Protocol (MCP) Mimarisi ve Bileşenleri
   - Yerel (Local) vs. Uzak (Remote) MCP Sunucuları
   - MCP Registry v0.1 Spesifikasyonu ve Azure API Center Entegrasyonu
   - MCP İzin Listeleri (Allow Lists: Allow All vs. Registry Only)
   - Yürütme Bağlamı Sınırları (Repository Scope, Branch Isolation, Permissions)
   - GitHub Agentic Workflows (`gh-aw` ve Continuous AI)
   - Özel Ajanlar (`.github/agents/*.agent.md`)
4. [Bölüm 4: Çoklu Ajan Sistemleri ve Orkestrasyon (Multi-Agent)](#bölüm-4-çoklu-ajan-sistemleri-ve-orkestrasyon-multi-agent)
   - Sorumluluk ve Kapsam Sınırları (Scope Boundaries)
   - Sıralı (Sequential) vs. Paralel (Parallel / Fan-Out Fan-In) Orkestrasyon
   - Eşzamanlılık Kontrolleri (Concurrency: Workflow vs. Branch Düzeyi)
   - Copilot Ajan Modları ve Paralellik Kapasitesi (Cloud vs. CLI vs. Local)
   - Çatışma Çözümü (Conflict Resolution) ve Tahkim (Arbitration)
   - Alt Ajanlar (Subagents) ve Devir Teslim (Handoffs) Sözdizimi
   - Canlı İzleme ve Hata Kurtarma (`gh agent-task view`, Bounded Retries, Escalation)
5. [Bölüm 5: Ajan Belleği, Durum Yönetimi ve Değerlendirme](#bölüm-5-ajan-belleği-durum-yönetimi-ve-değerlendirme)
   - Bellek Hiyerarşisi: Kısa Vadeli, Uzun Vadeli, Harici Bellek
   - Durum Çapası (State Anchor) Olarak Pull Request'ler
   - Bağlam Kayması (Context Drift) Tespiti ve Düzeltilmesi
   - Saklama Süreleri (Retention Policies: 90 Gün Kuralı, Public vs. Private)
   - Değerlendirme Sinyalleri ve Kalite Kapıları (Quality Gates, SARIF, Secret Scanning)
   - Kök Neden Analizi (Reasoning Errors, Tool Misuse, Context Issues)
6. [Bölüm 6: Yönetişim, Korkuluklar ve Operasyonel Güvenilirlik](#bölüm-6-yönetişim-korkuluklar-ve-operasyonel-güvenilirlik)
   - Risk Tabanlı Otonomi Modeli (Low, Medium, High, Critical)
   - En Düşük Yetki İlkesi (Least Privilege GITHUB_TOKEN)
   - CODEOWNERS ve Environment Korumaları (Approval Gates)
   - PreToolUse Hook Şemaları ve Komut Engelleme
   - Savunma Amaçlı (Defense-in-Depth) Bot Guardrail İş Akışları
   - Operasyonel Yönetişim Rutinleri (Haftalık, Aylık, Üç Aylık Döngüler)
   - Yönetişim Hata Kalıpları ve Anti-Pattern'ler

---

## BÖLÜM 1: AGENTIC AI TEMELLERİ VE GITHUB EKOSİSTEMİ

### 1.1 Asistan (Assistant) vs. Ajan (Agent) Ayrımı

| Özellik | AI Asistanı (Assistant) | Agentic AI (Ajan) |
| :--- | :--- | :--- |
| **Davranış Tarzı** | Reaktif (Prompt bekler, yanıt üretir, kontrolü kullanıcıya bırakır). | Hedefe Yönelik (Goal-driven; hedefi yorumlar, ara adımları planlar ve uygular). |
| **İşlem Yetkisi** | Yalnızca öneri, kod parçacığı veya açıklama üretir; doğrudan repo işlemi yapmaz. | Araçları (Tools/APIs) kullanarak kalıcı çıktılar üretir (branch açar, commit atar, PR oluşturur). |
| **İterasyon** | Kullanıcının sonraki sorusuna bağlıdır. | Sistem geri bildirimlerini (CI testleri, linter, güvenlik taramaları) okuyup kendi çıktısını düzelterek döngüde devam eder. |
| **GitHub'daki Varlığı** | Chat penceresinde öneri sunar; kullanıcı manuel kopyalar/uygular. | Bir GitHub katılımcısı gibi branch, PR, workflow çalıştırmaları ve inceleme yorumları üretir. |

### 1.2 Plan → Act → Evaluate Yaşam Döngüsü

Ajanik sistemler tek bir adımda durmaz; döngüsel bir akış izler:
1. **Plan (Planlama):**
   - Hedefi yorumlar, kapsamı ve riskleri belirler, başarı kriterlerini ve geri alma (rollback) planını tanımlar.
   - *GitHub Karşılığı:* PR açıklaması, Issue kontrol listesi veya `.github/pull_request_template.md` içinde açık, denetlenebilir plan çıktısı.
2. **Act (Yürütme):**
   - Planı doğrulanabilir adımlarla depoya uygular.
   - *GitHub Karşılığı:* Yeni bir izole branch oluşturma, dosya değişiklikleri, commit atma ve PR açma. Doğrudan korumalı ana dala (`main`) müdahale edilmez.
3. **Evaluate (Değerlendirme):**
   - Sonuçlar ajan kendi "özgüvenine" göre değil, sistem sinyallerine göre değerlendirilir.
   - *GitHub Karşılığı:* Workflow çalıştırmaları (build, test, lint), CODEOWNERS incelemeleri, SARIF güvenlik taramaları, secret scanning push korumaları.
   - Başarısızlık durumunda döngü başa döner (Plan revize edilir → Tekrar denenir) veya sınıra ulaşıldığında insana eskalasyon yapılır.

### 1.3 GitHub: System of Record ve Control Plane

- **System of Record (Kayıt Sistemi):** Ajanın niyetini, adımlarını ve kanıtlarını saklayan kalıcı hafızadır.
  - Repolar, dallar, commit geçmişi.
  - Issue'lar ve Tartışmalar (amaç ve iş bağlamı).
  - PR zaman çizelgesi, inceleme geçmişi ve kararlar.
  - GitHub Actions logları ve indirilebilir Artifact'lar.
- **Control Plane (Kontrol Düzlemi):** Ajanın ne yapabileceğini ve neyin kabul edileceğini belirleyen ve uygulayan politika uygulama noktalarıdır.
  - **Pull Requests:** Değişikliğin birleştirilmeden önce incelenmesini zorunlu kılar.
  - **Rulesets / Branch Protection:** Doğrudan push'ları engeller, zorunlu kontrolleri tanımlar.
  - **Required Status Checks:** CI testleri ve taramalar geçmeden merge edilmesini engeller.
  - **CODEOWNERS:** Hassas dosya yollarına (`infra/`, `.github/workflows/`) yetkili ekip onayını zorunlu kılar.
  - **Environments:** Dağıtım onay kapıları (approval gates) ve gizli anahtar (secrets) erişim sınırları sağlar.

### 1.4 Sorumluluk Modeli ve Katılımcı Modeli (Contributor Model)

- **Sorumluluk Dağıtımı:** Ajan yürütmeyi gerçekleştirir, ancak **sorumluluk insandadır**. Görevi tanımlayan, izinleri ayarlayan, kontrolleri yapılandıran ve PR'ı onaylayan ekip hesap verebilirdir.
- **Katılımcı Modeli (Contributor Model):**
  - Ajan çıktısı "özel bir AI standardı" ile değil, standart bir yazılım mühendisliği katkısı gibi değerlendirilmelidir.
  - *Aşırı Şüphecilik:* "AI yazdı, güvenilmez" diyerek baştan reddetmek yanlıştır.
  - *Aşırı Güven:* "Otomasyon yaptı / CI geçti, hemen merge et" demek büyük risktir.
  - **Değerlendirme Rubriği:** Amaç açık mı? Kapsam sınırlı mı? Zorunlu kontroller geçti mi? CODEOWNERS onayladı mı? Geri alma planı var mı?

---

## BÖLÜM 2: AJAN MİMARİSİ VE SDLC ENTEGRASYONU

### 2.1 SDLC Aşamalarına Ajan Sorumluluklarının Eşlenmesi

| SDLC Aşaması | Ajan Sorumluluğu | Birincil GitHub Yapısı / Denetim Yüzeyi |
| :--- | :--- | :--- |
| **Planning (Planlama)** | Kapsam taslağı, adımlar, başarı kriterleri, riskler | Issues, PR açıklamaları, Agents arayüzü |
| **Implementation (Geliştirme)** | İzole dal oluşturma, dosya düzenleme, PR açma | Dedicated Branch, Commits, Pull Request |
| **Validation (Doğrulama)** | Testleri çalıştırma, artifact yükleme, hatalarda düzeltme | Actions Workflow Runs, Status Checks, SARIF |
| **Deployment (Dağıtım)** | Genellikle kısıtlıdır; ajan sadece hazırlar, uygulayamaz | Environments, Deployment Approvals |

> **Altın Kural:** *Ajanlar önerir; insanlar ve repository kuralları kabul eder (Agents propose; humans and policy accept).*

### 2.2 Görev Sözleşmesi (Task Contract)

Her otonom ajan görevi 3 bileşene sahip olmalıdır:
1. **Inputs (Girdiler):** Issue içeriği, güvenlik uyarısı, izin verilen dosya yolları (`src/**`), kısıtlamalar (örn. `infra/` ve workflow dosyalarına dokunulamaz).
2. **Outputs (Çıktılar):** Yapılandırılmış bir plan, izole branch üzerindeki commit'ler, PR ve CI kanıt bağlantıları.
3. **Success Criteria (Başarı Kriterleri):** Yalnızca "CI passed" yeterli değildir; amaca yönelik olmalıdır (örn. "güvenlik açığı olan paket güncellendi ve kod taraması sıfır uyarı verdi").

### 2.3 Plan-First vs. Plan + Execution Karşılaştırması

- **Option A: Plan-First Pull Request:**
  - Ajan önce sadece plan içeren bir PR veya issue taslağı açar (kod değişikliği yoktur).
  - İnsanlar planı tartışır ve onaylar. Onay sonrası ajan uygulama dalına commit atar.
  - *Kullanım:* Yüksek riskli alanlar (`infra/`, `.github/workflows/`, kimlik doğrulama, üretim ayarları).
- **Option B: Plan + Execution:**
  - Ajan PR açıklamasında planı sunarken aynı zamanda ilk kod commit'lerini de içerir.
  - *Kullanım:* Düşük/orta riskli, kolayca geri alınabilir veya test kapsamı yüksek görevler.

### 2.4 GitHub Actions İş Akışı Mimarisi ve En İyi Pratikler

#### Veri Aktarımı: Step Outputs vs. Job Outputs vs. Env

- **Step Outputs:** Aynı iş (job) içindeki adımlar arasında veri aktarır (`$GITHUB_OUTPUT`).
- **Job Outputs:** Farklı işler arasında (`needs:` bağımlılığı ile) yapılandırılmış veri aktarır.
- **Environment Variables (`env`):** Çalışma ortamı yapılandırması içindir; veri akışı sözleşmesi olarak kullanılmamalıdır.

```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      plan_content: ${{ steps.gen.outputs.plan }}
    steps:
      - id: gen
        run: echo "plan=Refactor database queries" >> "$GITHUB_OUTPUT"

  implement:
    needs: plan
    runs-on: ubuntu-latest
    steps:
      - run: echo "Plan: ${{ needs.plan.outputs.plan_content }}"
```

#### GitHub Contexts Ayrımı

- `github.*`: Olay meta verileri ve çalışma anı kararları (örn. `github.event_name`, `github.ref`, `github.actor`).
- `vars.*`: Organizasyon veya repository düzeyinde tanımlı, yeniden kullanılabilir yapılandırma değişkenleri.
- `env.*`: İş veya adım düzeyinde tanımlanan ortam değişkenleri.

#### Savunma Amaçlı Tetikleyici Denetimi (Defensive Gating)

İş akışının birden fazla tetikleyicisi (`pull_request`, `workflow_dispatch`, `schedule`) olduğunda, PR'a özel adımların kazara patlamasını önlemek için job düzeyinde koşul eklenmelidir:

```yaml
jobs:
  validate-pr:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
```

---

## BÖLÜM 3: TOOLING, MCP VE YÜRÜTME ORTAMLARI

### 3.1 Model Context Protocol (MCP)

Model Context Protocol (MCP), AI ajanlarının dış araçlara ve hizmetlere bağlanmasını sağlayan açık standarttır. Ajanlar araçları keşfeder (discover), yapılandırılmış istek gönderir ve yapılandırılmış yanıt alır.

#### Yerel (Local) vs. Uzak (Remote) MCP Sunucuları

| Özellik | Local MCP Server | Remote MCP Server (HTTP) |
| :--- | :--- | :--- |
| **Çalıştığı Yer** | Geliştiricinin yerel makinesi veya runner (`http://localhost:3000`). | Uzak sunucuda barındırılır (`https://api.githubcopilot.com/mcp/`). |
| **Avantajı** | Yerel dosyalara, özel araçlara doğrudan erişim. | Kurulum gerektirmez, ekipler ve ortamlar arasında tutarlıdır. |
| **Kimlik Doğrulama** | Genellikle yerel bağlam, harici auth gerekmez. | Belirteç (token/OAuth) tabanlı yetkilendirme gerektirir. |
| **Destek** | GHES ve GHEC destekler. | GHEC (veri yerleşimi dahil) destekler. |

### 3.2 MCP Registry (Sunucu Kataloğu) ve v0.1 Spesifikasyonu

Organizasyonlar onaylı MCP sunucularını merkezi bir katalog üzerinden dağıtır.
- Özel bir MCP Registry kurmak için açık kaynak MCP Registry forku, Docker konteyneri veya özel bir servis kullanılabilir.
- Alternatif olarak **Azure API Center**, yönetilen (managed) bir MCP Registry olarak yapılandırılabilir.
- **Zorunlu HTTPS Uç Noktaları (Endpoints):**
  - `GET /v0.1/servers`
  - `GET /v0.1/servers/{serverName}/versions/latest`
  - `GET /v0.1/servers/{serverName}/versions/{version}`
- **Zorunlu CORS Başlıkları:**
  - `Access-Control-Allow-Origin: *`
  - `Access-Control-Allow-Methods: GET, OPTIONS`
  - `Access-Control-Allow-Headers: Authorization, Content-Type`

### 3.3 MCP İzin Listeleri (Allow Lists)

Kurumsal düzeyde (Enterprise/Organization) Copilot AI Controls menüsünden yönetilir:
- **Allow all:** Geliştiriciler herhangi bir MCP sunucusunu kısıtlama olmaksızın ekleyebilir.
- **Registry only:** Geliştiriciler **yalnızca** kayıt defterinde tanımlanmış onaylı sunucuları kullanabilir. Bu modda yerel (local) MCP sunucuları dahi registry'de listelenmek zorundadır ve sunucu ID'leri birebir eşleşmelidir!

### 3.4 Yürütme Bağlamı Sınırları (Execution Context Boundaries)

1. **Repository Scope:** Ajan yalnızca atandığı repo sınırları içinde çalışabilir; başka repolara erişemez.
2. **Branch Isolation:** Ajan doğrudan `main` üzerine yazamaz; daima özel bir daldan (`copilot/*`, `agent/*`) PR açar.
3. **Workflow Boundaries:** Ajan görevleri izole GitHub Actions runner'larında temiz bir konteyner ortamında yürütülür.
4. **Token Permissions:** `GITHUB_TOKEN` sınırları kullanılarak en düşük yetki ilkesi uygulanır.

### 3.5 GitHub Agentic Workflows (`gh-aw` / Continuous AI)

Geleneksel YAML iş akışları her adımı deterministik olarak tanımlarken, **GitHub Agentic Workflows** repo seviyesinde otonom süreçleri yürütür:
- **Yapısı:** İki ana bölümden oluşur:
  - **YAML Frontmatter (Korkuluklar):** Tetikleyiciler (`on`), izinler (`permissions`), araçlar (`tools`), ve güvenli çıktılar (`safe-outputs`).
  - **Markdown Gövdesi (Niyet/Intent):** İstenen iş sonucunu doğal dilde açıklar.
- **Derleme:** Markdown ve frontmatter, GitHub Actions tarafından çalıştırılan kilitli bir derleme dosyasına (`lock file`) dönüştürülür.
- **Temel Güvenlik Kalkanları:**
  - Varsayılan olarak salt-okunur (read-only) tokenler.
  - **Safe-outputs:** Ajan doğrudan issue/PR açamaz; çıktıyı önerir, ayrı ve kısıtlı bir adım bunu onaylayıp uygular.
  - Ajan çalışma sürecinde **sıfır secret (zero secrets)** bulunur.
  - Giden ağ istekleri için allowlist ve tehdit algılama (threat detection).

### 3.6 Özel Ajanlar (`.github/agents/*.agent.md`)

Depo düzeyinde uzmanlaşmış ajan tanımları:
```markdown
---
applyTo:
  - '**/*.js'
  - 'src/auth/**'
tools:
  - read_file
  - search_files
---
Sen kimlik doğrulama kodlarını inceleyen bir güvenlik ajanısın...
```
- `applyTo`: Ajanın odaklanacağı dosya yollarını kısıtlar.
- `tools`: Ajanın kullanabileceği araçları sınırlar.
- *Dikkat:* Özel ajanlar dal oluşturma veya PR açma davranışını doğrudan kontrol etmez; bunu onları çalıştıran yürütme ortamı (orchestrator/workflow) yönetir.

---

## BÖLÜM 4: ÇOKLU AJAN SİSTEMLERİ VE ORKESTRASYON

### 4.1 Çoklu Ajan Sorumluluk Modeli

Ajanların çatışmasını önlemek için kapsam sınırları (scope boundaries) tanımlanmalıdır:
- **Dependency Agent:** Yalnızca bağımlılık bildirimlerini (`package.json`, `pom.xml`) ve kilit dosyalarını (`package-lock.json`) günceller; `src/` koduna dokunmaz.
- **Refactoring Agent:** Yalnızca `src/` altındaki kodları günceller; workflow veya bağımlılık dosyalarına dokunmaz.
- **Security / Review Agent:** Yalnızca tarama ve doğrulama yapar; rapor üretir veya salt-okunur öneri sunar.

### 4.2 Orkestrasyon Kalıpları: Sıralı ve Paralel (Fan-Out / Fan-In)

1. **Sıralı (Sequential) Orkestrasyon:**
   - Bir ajan PR açar → CI çalışır → CI tamamlanınca güvenlik ajanı tetiklenir (`workflow_run` olayı):
   ```yaml
   on:
     workflow_run:
       workflows: ["CI Validation"]
       types: [completed]
   ```
2. **Paralel Fan-Out / Fan-In Orkestrasyonu (Sınavda Özellikle Sorulur!):**
   - Birden fazla analiz ajanı paralel çalışır (Fan-Out).
   - Birleştirici iş (`plan_merger`), `needs: [spec_analyzer, risk_reviewer]` ile her ikisinin tamamlanmasını bekler ve çıktıları birleştirir (Fan-In).

### 4.3 Eşzamanlılık (Concurrency) Yönetimi

PR üzerinde sık commit atıldığında eski iş akışlarının kaynak tüketmesini ve çakışmasını engellemek için iş akışı düzeyinde concurrency tanımlanır:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
> **Önemli Not:** `group` ifadesinde yalnızca `${{ github.ref }}` kullanılırsa, aynı daldaki tüm farklı iş akışları birbirini engelleyebilir! Bu yüzden `${{ github.workflow }}-${{ github.ref }}` şeklinde kapsam belirlenmelidir.

### 4.4 Copilot Ajan Modları ve Paralellik Kapasitesi

| Ajan Çalışma Modu (Agent Mode) | Birden Fazla Görevde Paralel Oturum Açabilir mi? |
| :--- | :--- |
| **Copilot Cloud** | **Evet** (Paralel oturumları destekler) |
| **Copilot CLI** | **Evet** (Paralel oturumları destekler) |
| **Local (IDE)** | **Hayır** (Yalnızca sıralı / serial; tek tek çalışır) |

### 4.5 Çatışma Çözümü (Conflict Resolution) ve Tahkim (Arbitration)

- **Tahkim Kuralı:** İki ajan aynı dosyada çakışıyorsa veya yarış durumuna (race condition) giriyorsa, "ilk merge olan kazanır" mantığı bir anti-pattern'dir.
- **Merge Doğrulama Kontrolü (Merge Validation Check):** PR içinde ana dalla birleşimin temiz olduğunu doğrulamak için `git merge --no-commit origin/main` adımı zorunlu kontrol yapılır.
- **Eskalasyon Eşiği:** Bir ajan dalı rebase sonrası üst üste **2 kez** çakışırsa veya aynı hata imzasıyla **2 kez** başarısız olursa, otomatik deneme durdurulur ve insan müdahalesine eskalasyon yapılır.

### 4.6 Alt Ajanlar (Subagents) ve Handoff Sözdizimi

Ana ajan dosyasında (`planner.agent.md`):
```yaml
---
agents: [implementer, code-review]
handoffs:
  - label: Start Implementation
    agent: implementer
    send: true
    model: GPT-5.2
  - label: Run Review
    agent: code-review
    prompt: Review the code changes made in the previous step.
---
```
- `disable-model-invocation: true`: Ajanın bir alt ajan olarak çağrılmasını engeller.
- `user-invocable: false`: Ajanın kullanıcı tarafından arayüzde doğrudan seçilmesini engeller.
- **Ruleset Bypass Aktörü:** Ajan branch'lerine push yaparken commit imzalama kuralı engeline takılıyorsa, ruleset ayarlarında "GitHub Copilot" bypass aktörü olarak tanımlanabilir.

---

## BÖLÜM 5: AJAN BELLEĞİ, DURUM YÖNETİMİ VE DEĞERLENDİRME

### 5.1 Bellek Hiyerarşisi

1. **Short-Term Memory (Kısa Vadeli Bellek):** Oturum içi bağlamdır (mevcut prompt, son araç yanıtları). Oturum bittiğinde silinir.
2. **Long-Term Memory (Uzun Vadeli Bellek):** Oturumlar arası yeniden kullanılabilir küratörlü bilgi (tasarım şablonları, talimat dosyaları, mimari kurallar).
3. **External Memory (Harici Bellek - Source of Truth):** Sistemin kalıcı hafızasıdır. GitHub üzerinde yaşar:
   - Gereksinimler & Kabul Kriterleri → **Issue**
   - Kararlar & Mevcut İlerleme Durumu → **Pull Request**
   - Doğrulama Kuralları → **Repository Instructions / Rules**
   - Sonuçlar ve Kanıtlar → **Workflow Runs & Artifacts**

### 5.2 Bağlam Kayması (Context Drift)

- **Tanım:** Ajanın ürettiği değişikliklerin zamanla orijinal hedeften, kabul kriterlerinden veya önceki mimari kararlardan uzaklaşmasıdır.
- **Tespiti:** PR diff'i ile Issue kriterleri uyuşmadığında, önceki kararlarla çelişen commit'ler atıldığında veya testler başarısız olduğunda anlaşılır.
- **Düzeltilmesi:** Ajan oturum geçmişine değil, "Source of Truth" olan Issue veya PR açıklamasına yeniden çıpalanır (re-anchor). Gerekirse PR açıklaması güncellenir veya bellek sıfırlanır (reset).

### 5.3 Saklama Süreleri (Retention Policies)

- GitHub Actions logları ve artifact'ları varsayılan olarak **90 gün** saklanır ve ardından otomatik olarak kalıcı olarak silinir.
- **Public Repolar:** 1 ile 90 gün arasında yapılandırılabilir.
- **Private Repolar:** 1 ile **400 güne kadar** uzatılabilir.
- Silinen bir artifact geri getirilemez.
- Bir artifact'ın silinip silinmediği GitHub Organizasyon Denetim Günlüğünde (Audit Log) `action:artifact.destroy` olayı sorgulanarak tespit edilir.

### 5.4 Değerlendirme ve Kök Neden Analizi (Root Causes)

Ajan hataları 3 ana grupta sınıflandırılır:
1. **Reasoning Errors (Muhakeme Hataları):** Gereksinimlerin yanlış yorumlanması, mantık hatası kurulması, kabul kriterlerinin göz ardı edilmesi. (*Çözüm: Prompt ve repo talimatlarını netleştirmek*).
2. **Tool Misuse (Araç Kötüye Kullanımı):** Yanlış CLI komutu çalıştırma, geçersiz argüman gönderme, workflow tetikleme hataları. (*Çözüm: Araç kısıtlamalarını ve parametre şablonlarını güncellemek*).
3. **Context Issues (Bağlam Sorunları):** Güncel olmayan dal bilgisi kullanma, çelişkili bilgilere dayanma, silinmiş loglara referans verme. (*Çözüm: Issue/PR'a yeniden çıpalama, dalı rebase etme*).

---

## BÖLÜM 6: YÖNETİŞİM, KORKULUKLAR VE OPERASYONEL GÜVENİLİRLİK

### 6.1 Risk Tabanlı Otonomi Modeli

| Risk Seviyesi | Örnek Eylemler | Önerilen Kontrol ve Otonomi Düzeyi |
| :--- | :--- | :--- |
| **Low (Düşük)** | Dokümantasyon (`docs/`), kod formatlama | **Full Automation:** Gerekli kontroller geçtikten sonra GitHub Auto-merge ile otomatik birleştirilebilir. |
| **Medium (Orta)** | `src/` kod değişiklikleri, rutin bağımlılık güncellemeleri | **PR + Required Checks:** Zorunlu CI kontrolleri ve en az 1 onay gereklidir. |
| **High (Yüksek)** | Altyapı (`infra/`), iş akışları (`.github/workflows/`), güvenlik ayarları | **CODEOWNERS + Human Review:** İlgili ekipten zorunlu onay, katı ruleset kuralları. |
| **Critical (Kritik)** | Production dağıtımları, production secret erişimi | **Environment Approval Gate:** Ajan yalnızca dağıtımı hazırlar; onay olmadan asla çalıştırılamaz. |

### 6.2 En Düşük Yetki İlkesi (Least Privilege GITHUB_TOKEN)

İş akışı düzeyinde varsayılan izinler salt-okunur (`read-all` veya `contents: read`) yapılmalı, yazma yetkisi yalnızca ilgili işe (job) verilmelidir:

```yaml
permissions:
  contents: read

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Salt okunur analiz"

  publish_pr:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - run: echo "PR açma ve yazma yetkisi"
```

### 6.3 Copilot CLI Araç Kapsamı ve PreToolUse Kancaları (Hooks)

- **CLI Araç Kısıtlaması:** Salt okunur görevlerde yazma araçları engellenir:
  `copilot -p "Son commit'leri incele" --allow-tool 'shell(git)'`
- **PreToolUse Hook ile Komut Engelleme:**
  `.github/hooks/` altında tanımlanan hook'lar, tehlikeli komutları çalıştırılmadan önce bloklar:
  ```json
  {
    "hook": "preToolUse",
    "tools": ["shell(bash)"],
    "rules": [
      { "match": "sudo", "permissionDecision": "deny" },
      { "match": "rm -rf /", "permissionDecision": "deny" },
      { "match": "curl .*\\|\\s*bash", "permissionDecision": "deny" }
    ]
  }
  ```

### 6.4 Savunma Amaçlı Guardrail: Bot PR'larının Otomatik Birleşmesini Engelleme

Ajanların açtığı PR'ların yalnızca bot onaylarıyla birleşmesini engellemek için `actions/github-script` ile insan incelemesi zorunlu kılınabilir:

```yaml
jobs:
  enforce-human-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            const reviews = await github.rest.pulls.listReviews({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.payload.pull_request.number
            });
            const approvedByHuman = reviews.data.some(r =>
              r.state === "APPROVED" &&
              r.user &&
              r.user.type === "User" &&
              r.user.login !== "github-copilot[bot]"
            );
            if (!approvedByHuman) {
              core.setFailed("Bu PR bir insan kullanıcı tarafından onaylanmalıdır!");
            }
```

### 6.5 Operasyonel Yönetişim Rutinleri (Governance Cadence)

1. **Haftalık (Weekly):** Başarısız olan ajan iş akışı çalıştırmalarının ve politika ihlallerinin incelenmesi.
2. **Aylık (Monthly):** GITHUB_TOKEN izinlerinin ve ortam bazlı gizli anahtar (secrets) kapsamlarının gözden geçirilmesi.
3. **Üç Aylık (Quarterly):** Repository ruleset kuralları, CODEOWNERS dosyaları, environment onaylayıcıları ve log saklama politikalarının denetlenmesi.

### 6.6 Temel Yönetişim Anti-Pattern'leri (Sınavda Çıkar!)

1. **Planless Execution (Plansız Yürütme):** Ajanın açık bir hedef ve plan sunmadan doğrudan kod diff'i üretmesi.
2. **Hidden Reasoning (Gizli Akıl Yürütme):** Ajanın kararlarının, varsayımlarının ve ara adımlarının PR veya loglarda yer almaması.
3. **Unbounded Autonomy (Sınırsız Otonomi):** Ajanın production dağıtımı veya infra değişikliğini onay almadan yapabilmesi.
4. **Excess Permissions (Aşırı İzinler):** Ajan iş akışlarına `write-all` izni verilmesi.
5. **Rubber-Stamping (Körlemesine Onaylama):** İncelemecilerin CI geçtiği için kanıtları ve kodu incelemeden onay vermesi.
6. **Bypass Paths Exist (Bypass Yollarının Açık Olması):** Korunan dallara doğrudan push yapılabilmesi veya kontrollerin atlanabilmesi.

---
*Bu doküman GH-600 sınav hazırlığı için tüm modüllerin sentezlenmesiyle oluşturulmuştur.*
