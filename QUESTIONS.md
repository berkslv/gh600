# GitHub Certified: Agentic AI Developer (GH-600) - 50 Soru Deneme Sınavı

Bu doküman, **Course GH-600T00-A: Developing in Agentic AI Systems** ve **GitHub Certified: Agentic AI Developer** sertifika sınavı standartlarında hazırlanmış **50 adet senaryo tabanlı** soru içermektedir. Sorular gerçek Microsoft / GitHub sertifika sınavlarının zorluk derecesine, soru kalıplarına ve teknik derinliğine birebir uygundur.

---

### Soru 1 (Tek Seçim - Temel Kavramlar)
Bir yazılım geliştirme ekibi, repolarında GitHub Copilot kullanımını genişletmektedir. Ekip lideri, bazı görevlerde Copilot'un bir "Asistan (Assistant)" olarak mı yoksa bir "Ajan (Agent)" olarak mı davrandığını ayırt etmek istemektedir.

Aşağıdakilerden hangisi bir yapay zeka sisteminin GitHub üzerinde **ajan (agent)** olarak davrandığının en açık göstergesidir?

A) Geliştiriciye IDE chat penceresinde karmaşık bir fonksiyon için kod önerisi sunması  
B) Bir güvenlik açığı bildirimini inceleyerek yeni bir dal (branch) açması, bağımlılığı güncellemesi ve doğrulama kanıtlarıyla birlikte bir Pull Request oluşturması  
C) Terminalde çalıştırılan bir komutun hata çıktısını açıklayıp geliştiriciye dokümantasyon bağlantıları vermesi  
D) Bir Pull Request içeriğindeki kod değişikliklerini inceleyip geliştirici için özet metin üretmesi  

> **Doğru Cevap:** **B**  
  **Açıklama:** Asistanlar (Assistants) reaktiftir; öneri sunar, açıklar veya özetler fakat depo üzerinde bağımsız bir işlem yürütmez. Ajanlar (Agents) ise hedefe yöneliktir (goal-driven); bir hedefi yorumlar, ara adımları belirler, araçları (APIs, workflows) kullanır ve branch, commit ve PR gibi kalıcı çıktılar üretir.

---

### Soru 2 (Tek Seçim - Yaşam Döngüsü)
Bir otonom ajan, `src/auth/` dizinindeki bir açığı gidermek üzere görevlendirilmiştir. Ajan Plan → Act → Evaluate yaşam döngüsünü takip etmektedir.

Ajanın **Evaluate (Değerlendirme)** aşamasında uyması gereken temel mimari ilke aşağıdakilerden hangisidir?

A) Ajan, kod değişikliğini kendi LLM modelinin tahmin güven skoruna (confidence score) göre onaylamalıdır.  
B) Ajan, değişikliği doğrudan `main` dalına merge edip üretim loglarını izlemelidir.  
C) Değerlendirme, ajanın özgüvenine değil; GitHub Actions workflow çalıştırmaları, zorunlu durum kontrolleri (status checks) ve SARIF güvenlik taramaları gibi nesnel sistem sinyallerine dayanmalıdır.  
D) Ajan, değişiklikleri PR açmadan önce yerel makinede çalıştırmalı ve logları harici bir S3 bucket'ına yüklemelidir.  

> **Doğru Cevap:** **C**  
> **Açıklama:** GH-600 mimari standardına göre ajanın değerlendirme aşaması, modelin kendi doğruluğuna olan güvenine değil; CI testleri, linter, SARIF kod taraması ve secret scanning gibi GitHub kontrol düzleminin ürettiği doğrulanabilir sistem sinyallerine dayanmalıdır.

---

### Soru 3 (Tek Seçim - Sorumluluk Modeli)
Bir ajan tarafından açılan ve CI kontrollerinden başarıyla geçen bir Pull Request, üretim ortamında beklenmeyen bir kesintiye (outage) yol açmıştır.

GitHub'ın katılımcı ve sorumluluk yönetişim modeline göre, bu olaydaki nihai hesap verebilirlik (accountability) kime aittir?

A) Ajanı geliştiren üçüncü taraf model sağlayıcısına  
B) Görevi tanımlayan, izinleri belirleyen, kontrolleri kurgulayan ve PR'ı merge eden insan mühendislik ekibine  
C) GitHub Actions runner altyapısına  
D) Yalnızca PR'ı oluşturan GitHub App bot kimliğine  

> **Doğru Cevap:** **B**  
> **Açıklama:** Yürütme (execution) ajana devredilebilir ancak sorumluluk (accountability) sisteme devredilemez. Görevi veren, izin sınırlarını çizen, kalite kapılarını belirleyen ve PR'ı onaylayarak birleştiren insan ekipleri nihai olarak sorumludur.

---

### Soru 4 (Tek Seçim - Anti-Pattern Tespiti)
Bir kod inceleme uzmanı, bir ajanın açtığı PR'ı incelerken PR açıklamasında hiçbir niyet, kapsam, adım veya geri alma planı bulunmadığını, yalnızca 40 dosyayı kapsayan büyük bir diff bulunduğunu fark etmiştir.

Bu durum GH-600 müfredatında hangi anti-pattern olarak adlandırılır?

A) Blind trust in automation  
B) Planless execution (Plansız Yürütme)  
C) Context drift  
D) Over-permissioned agent  

> **Doğru Cevap:** **B**  
> **Açıklama:** Ajanın incelenebilir yapılandırılmış bir yaklaşım sunmadan doğrudan kod değişikliklerine girişmesi "Planless execution" anti-pattern'idir. İnceleyicilerin amacı anlamasını imkansızlaştırır.

---

### Soru 5 (Tek Seçim - Katılımcı Modeli)
Katılımcı Modeli (Contributor Model) ilkelerine göre bir ekip, ajan tarafından oluşturulan Pull Request'leri nasıl değerlendirmelidir?

A) Yazar bir yapay zeka olduğu için otomatik olarak reddedilmeli veya baştan şüpheyle yaklaşılmalıdır.  
B) CI testleri başarılı olduğu sürece kod satırları incelenmeden otomatik merge edilmelidir.  
C) Değişiklik, yazarın kimliğinden bağımsız olarak standart bir insan mühendislik katkısı gibi; kapsamı, niyetin karşılanması, zorunlu kontrolleri ve CODEOWNERS onayları açısından değerlendirilmelidir.  
D) Ajan PR'ları yalnızca haftalık toplu (batch) inceleme toplantılarında incelenmelidir.  

> **Doğru Cevap:** **C**  
> **Açıklama:** Contributor Model iki uç hatayı engeller: aşırı şüphecilik ve otomasyona körü körüne güven. Ajan çıktısı, deponun "Definition of Done" kriterlerine göre tıpkı standart bir geliştirici katkısı gibi denetlenmelidir.

---

### Soru 6 (Çoklu Seçim - İki Seçenek: Risk Azaltma)
Bir şirkette ajanların GitHub üzerinde çalışırken oluşturabileceği riskleri en aza indirmek ve izlenebilirliği (traceability) sağlamak istenmektedir.

Asgari bir denetim izi (minimum audit trail) oluşturmak için Pull Request içinde hangi iki unsurun yer alması **zorunludur**? (Her doğru seçenek çözümün bir parçasını sunar.)

A) Ajanın özel çalışma anı LLM düşünce zinciri (chain-of-thought) prompt loglarının ham metni  
B) İlgili Issue veya hedefe bağlantı içeren açık bir niyet ve incelenebilir bir plan  
C) Ajanın yerel makinesindeki CPU ve RAM tüketim grafikleri  
D) Zorunlu kontrolleri ve iş akışı çalıştırmalarını gösteren doğrulanabilir CI bağlantıları ve artifact'lar  
E) Depodaki tüm kullanıcıların kişisel erişim belirteçleri (PAT)  

> **Doğru Cevap:** **B ve D**  
> **Açıklama:** Minimum denetim izi; belirtilen hedef (issue bağlantısı), incelenebilir plan, sınırlandırılmış changeset, otomatik kanıtlar (workflow run/artifacts) ve insan inceleme kararından oluşur. Ham düşünce zinciri veya makine metrikleri repo düzeyinde zorunlu denetim izi bileşeni değildir.

---

### Soru 7 (Tek Seçim - Kontrol Düzlemi)
Hassas bir depoda `/.github/workflows/` dizinindeki YAML dosyalarında yapılacak herhangi bir değişikliğin doğrudan platform mühendisliği ekibinin onayına tabi olması istenmektedir.

Bu gereksinimi GitHub-native olarak en doğrudan karşılayan mekanizma aşağıdakilerden hangisidir?

A) GitHub Issues etiketleri  
B) CODEOWNERS dosyası ve Ruleset üzerinde "Require review from Code Owners" kuralının etkinleştirilmesi  
C) Depo ana sayfasındaki README.md uyarı metni  
D) İş akışına `continue-on-error: true` eklenmesi  

> **Doğru Cevap:** **B**  
> **Açıklama:** CODEOWNERS dosyası, dosya yollarına göre ilgili ekipleri otomatik olarak incelemeci atar. Ruleset/Branch Protection ile "Require review from Code Owners" açıldığında, ilgili ekibin onayı olmadan PR merge edilemez.

---

### Soru 8 (Tek Seçim - System of Record)
Aşağıdakilerden hangisi GitHub'ın bir ajan sistemi için "System of Record (Kayıt Sistemi)" olma fonksiyonunu en iyi açıklar?

A) Tüm kod derlemelerini bulutta en yüksek işlemci gücüyle çalıştırması  
B) Ajanın niyetini, planlarını, dal geçmişini, PR tartışmalarını, inceleme kararlarını ve iş akışı kanıtlarını kalıcı ve denetlenebilir biçimde saklaması  
C) Kodlama hatalarını yapay zeka modellerine ihtiyaç duymadan otomatik olarak düzeltmesi  
D) Tüm üçüncü taraf API'lerin kimlik bilgilerini şifresiz olarak önbelleğe alması  

> **Doğru Cevap:** **B**  
> **Açıklama:** GitHub, hem kalkınma sürecini yürütür hem de ajan davranışlarının geriye dönük denetlenebilmesi (post-hoc analysis) için tüm niyet, plan, commit, PR ve workflow kanıtlarını saklayan resmi kayıt sistemidir.

---

### Soru 9 (Tek Seçim - SDLC Sorumluluk Eşlemesi)
Bir ekip bağımlılık açığı giderme (dependency remediation) ajanını devreye almaktadır. Ajanın görev kapsamı mimari olarak yalnızca "Implementation (Geliştirme)" aşamasıyla sınırlandırılmıştır.

Bu tasarıma göre ajanın görevi ne zaman tamamlanmış sayılır?

A) Bağımlılık paketini güncelleyip doğrudan `main` dalına push yaptığında ve prodüksiyona çıktığında  
B) İlgili bağımlılığı ve lockfile dosyasını yeni bir dalda güncelleyip yapılandırılmış plan içeren bir PR açtığında  
C) Kod incelemelerini kendi kendine onaylayıp merge ettiğinde  
D) Şirketin bulut ortamındaki Kubernetes cluster'ını yeniden başlattığında  

> **Doğru Cevap:** **B**  
> **Açıklama:** Implementation ile sınırlandırılmış bir ajan dalı oluşturur, dosyaları günceller ve PR açar. Doğrulama (Validation) CI sistemine, kabul ve merge işlemi ise insan inceleyicilere ve politikalara aittir.

---

### Soru 10 (Tek Seçim - Plan-First Yaklaşımı)
Kritik bir ödeme altyapısı deposunda ajanların kod geliştirmeden önce mutlaka insan onayı alması istenmektedir. Mimari ekip "Plan-first pull request" yaklaşımını seçmiştir.

Bu yaklaşımın operasyonel işleyişi nasıldır?

A) Ajan tüm kodları yazar, PR açar ve aynı anda prodüksiyona dağıtır.  
B) Ajan önce yalnızca plan içeren bir PR açar (kod değişikliği içermez); plan insanlar tarafından tartışılıp onaylandıktan sonra ajan uygulama adımlarına geçer.  
C) Ajan kodları doğrudan main dalına gönderir ve PR açıklamasına plan yazar.  
D) Geliştiriciler planı yazar, ajan ise sadece linter çalıştırır.  

> **Doğru Cevap:** **B**  
> **Açıklama:** Plan-first modelinde niyet (intent) ile yürütme (execution) birbirinden ayrılır. Kod yazılmadan önce niyet doğrulanır; böylece risk erken aşamada sınırlandırılır.

---

### Soru 11 (Tek Seçim - Plan Gate Workflow)
Bir repoda ajanların açtığı PR'larda `.github/pull_request_template.md` şablonuna uygun bir planın bulunmasını teknik olarak zorunlu kılmak istiyorsunuz.

Bu kuralı bağlayıcı bir sistem güvencesine dönüştürmek için ne yapılmalıdır?

A) PR şablonunun içine "Lütfen plan ekleyin" şeklinde bir yorum satırı yazılmalıdır.  
B) Geliştiricilere e-posta gönderilmelidir.  
C) Plan dosyasının veya PR açıklamasındaki plan bloğunun varlığını kontrol eden bir GitHub Actions iş akışı yazılmalı ve bu iş akışı repository ruleset / branch protection altında "Required Status Check" yapılmalıdır.  
D) CODEOWNERS dosyasına ajan botunun adı eklenmelidir.  

> **Doğru Cevap:** **C**  
> **Açıklama:** Yalnızca şablon koymak tavsiye niteliğindedir. Bir kuralın sistemsel olarak atlanamaz olmasını sağlamak için bir doğrulama iş akışı yazılmalı ve bu iş akışı "Required Status Check" olarak işaretlenmelidir.

---

### Soru 12 (Tek Seçim - GitHub Actions Veri İletişimi)
Ajanik bir iş akışında `plan` işi (job) tarafından üretilen bir metin çıktısının, downstream konumdaki `implement` işi tarafından okunması gerekmektedir.

GitHub Actions mimarisinde işler arası (cross-job) veri paylaşımını sağlamak için hangi mekanizma kullanılmalıdır?

A) Step düzeyinde tanımlanan yerel Linux environment değişkenleri  
B) `GITHUB_OUTPUT` dosyasına yazılan ve iş düzeyinde `outputs` bloğu ile dışa aktarılan değerler ve bağımlı işte `needs.<job_id>.outputs.<output_name>` kullanımı  
C) Veriyi depodaki `README.md` dosyasına commit atmak  
D) GitHub Issues API üzerinden yorum bırakmak  

> **Doğru Cevap:** **B**  
> **Açıklama:** İşler arası yapılandırılmış veri aktarımı job-level `outputs` ve `needs` sözdizimi ile gerçekleştirilir. Step output'ları sadece aynı job içindeki adımlar arasında geçerlidir; `env` ise çalışma anı yapılandırması içindir.

---

### Soru 13 (Tek Seçim - Defensive Gating)
Aşağıdaki iş akışı tanımını inceleyiniz:

```yaml
name: Agent PR Processor
on:
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  comment-plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Comment on PR
        run: gh pr comment --body "Plan analyzed."
```

Bu iş akışı manuel olarak (`workflow_dispatch`) tetiklendiğinde `Comment on PR` adımı PR bağlamı bulunmadığı için hata verecektir.

Bunu engellemek için hangi "Defensive Gating" koşulu eklenmelidir?

A) Job düzeyinde: `if: github.event_name == 'pull_request'`  
B) Step düzeyinde: `continue-on-error: true`  
C) Trigger düzeyinde: `branches-ignore: [main]`  
D) Permissions düzeyinde: `contents: none`  

> **Doğru Cevap:** **A**  
> **Açıklama:** Defensive gating, iş akışının PR'a özgü adımlarının yalnızca gerçek bir PR olayıyla tetiklendiğinde çalışmasını güvence altına almak için `if: github.event_name == 'pull_request'` koşulunun kullanılmasıdır.

---

### Soru 14 (Tek Seçim - Görev Sözleşmesi: Başarı Kriteri)
Bir güvenlik ajanı, CVE açığı bulunan bir npm paketini güncellemekle görevlendirilmiştir. Ajan paketi `package.json` içinde güncellemiş ve `npm test` komutu başarıyla geçmiştir. Ancak güvenlik tarayıcısı, açığın geçişli (transitive) bir alt bağımlılık üzerinden halen erişilebilir olduğunu bildirmektedir.

Bu durum ajanik sistem tasarımında hangi temel prensibi ihlal eder?

A) En düşük yetki ilkesini  
B) Başarı kriterlerinin sadece "CI passed" olarak değil, asıl amaca yönelik (vulnerability resolved) tanımlanması gerekliliğini  
C) Branch isolation kuralını  
D) Concurrency kontrollerini  

> **Doğru Cevap:** **B**  
> **Açıklama:** "CI passed" gereklidir fakat her zaman yeterli değildir. Başarı kriterleri görevin gerçek hedefini (güvenlik açığının tamamen kapanması) doğrulamalıdır; salt testlerin yeşil olması açığın kapandığını kanıtlamaz.

---

### Soru 15 (Tek Seçim - Kancalar / Hooks)
GitHub Copilot ajanlarında `.github/hooks/` dizini altında tanımlanan bir `preToolUse` kancasının (hook) temel amacı nedir?

A) Ajanın her işleminden sonra ekrana başarı mesajı yazdırmak  
B) Ajan tehlikeli bir araç veya kabuk komutu (örn. `rm -rf /` veya `sudo`) çalıştırmadan önce araya girerek işlemi denetlemek ve gerekirse yürütmeyi engellemek  
C) GitHub Actions runner'larını otomatik olarak kapatmak  
D) Kullanıcının GitHub parolasını sıfırlamak  

> **Doğru Cevap:** **B**  
> **Açıklama:** `preToolUse` hook'ları, modelin mantığına veya prompt talimatlarına güvenmek yerine, araç çalıştırılmadan hemen önce deterministik kurallarla tehlikeli komutları bloke eden teknik korkuluklardır (technical guardrails).

---

### Soru 16 (Tek Seçim - Context Seçimi)
Bir GitHub Actions iş akışında, iş akışını tetikleyen olayın türünü ve referans dalını belirlemek için hangi context kullanılmalıdır?

A) `vars.*`  
B) `env.*`  
C) `github.*`  
D) `secrets.*`  

> **Doğru Cevap:** **C**  
> **Açıklama:** Olay meta verileri (`event_name`, `ref`, `actor` vb.) `github.*` context'i altındadır. `vars.*` yapılandırma değişkenleri, `env.*` çalışma ortamı değişkenleri, `secrets.*` ise şifreli değerler içindir.

---

### Soru 17 (Tek Seçim - Artifact Tabanlı Kanıt Paylaşımı)
Ajanik iş akışlarında oluşturulan test sonuçları, plan dosyaları ve tarama raporlarının depoya commit atılmadan diğer işler veya insan inceleyiciler tarafından erişilebilir kılınması istenmektedir.

Bunun için önerilen GitHub Actions deseni nedir?

A) Çıktıları geçici olarak genel bir web sitesine POST etmek  
B) Çıktıyı üreten işte `actions/upload-artifact@v4` kullanmak, tüketen veya inceleyen tarafta ise `actions/download-artifact@v4` ile indirmek  
C) Dosyaları `main` dalına doğrudan push etmek  
D) Verileri base64 formatına çevirip commit mesajına eklemek  

> **Doğru Cevap:** **B**  
> **Açıklama:** Artifact'lar, oluşturulan dosyaların kalıcı ve incelenebilir olmasını sağlar; depoya gereksiz ikili veya geçici dosyalar commit edilmesini önler.

---

### Soru 18 (Tek Seçim - Model Context Protocol Nedir?)
Model Context Protocol (MCP) mimarisi hakkında aşağıda verilen ifadelerden hangisi **doğrudur**?

A) Yalnızca yerel makinelerde çalışan tescilli bir GitHub Actions eklentisidir.  
B) AI istemcilerinin harici araçları ve veri kaynaklarını standart bir protokol üzerinden keşfetmesini, yapılandırılmış istek gönderip yanıt almasını sağlayan açık bir protokoldür.  
C) LLM modellerinin ağırlıklarını (weights) sıkıştırmak için kullanılan bir donanım standardıdır.  
D) GitHub Secrets yerine şifre saklayan bir veritabanıdır.  

> **Doğru Cevap:** **B**  
> **Açıklama:** MCP, AI ajanları ile harici araç ve servisler arasında standart bir iletişim katmanı sunar. Ajanın dış dünyadaki yetenekleri tutarlı bir formatta keşfetmesini ve çalıştırmasını sağlar.

---

### Soru 19 (Tek Seçim - MCP Registry Endpoints)
Bir organizasyon, kendi özel MCP Registry (Kayıt Defteri) servisini geliştirmektedir. Sistemin GitHub Copilot ile tam uyumlu çalışabilmesi için **MCP Registry v0.1** spesifikasyonuna göre aşağıdaki HTTP GET uç noktalarından hangisini sağlaması **zorunludur**?

A) `GET /api/v2/tools/all`  
B) `GET /v0.1/servers`  
C) `GET /mcp/download/binary`  
D) `GET /copilot/license/check`  

> **Doğru Cevap:** **B**  
> **Açıklama:** MCP Registry v0.1 spesifikasyonuna göre zorunlu uç noktalar: `GET /v0.1/servers`, `GET /v0.1/servers/{serverName}/versions/latest` ve `GET /v0.1/servers/{serverName}/versions/{version}` şeklindedir.

---

### Soru 20 (Tek Seçim - Azure API Center MCP Entegrasyonu)
Bir kurumsal müşteri, MCP sunucularını yönetmek için **Azure API Center** servisini yönetilen bir MCP Registry olarak kullanmak istemektedir.

GitHub Enterprise AI Controls üzerinde Azure API Center yapılandırılırken aşağıdaki kurallardan hangisine dikkat edilmelidir?

A) Kayıt defteri URL alanına tam endpoint olarak `/v0.1/servers` yolu eklenmelidir.  
B) Kayıt defteri URL alanına yalnızca taban URL (base URL) girilmeli (`/v0.1/servers` eklenmemeli) ve anonim erişim etkinleştirilmelidir.  
C) Azure API Center yalnızca SSH protokolü üzerinden bağlanabilir.  
D) Azure API Center kullanıldığında Copilot CLI devre dışı bırakılmalıdır.  

> **Doğru Cevap:** **B**  
> **Açıklama:** Dokümantasyona göre Azure API Center kullanıldığında temel (base) URL girilir (`/v0.1/servers` yolu eklenmez) ve Copilot'un listeyi çekebilmesi için anonim erişim açık olmalıdır.

---

### Soru 21 (Tek Seçim - MCP Allow Lists)
Bir kurumda Copilot politikası "Registry only" olarak ayarlanmıştır. Geliştiricilerden biri yerel makinesinde `http://localhost:3000` üzerinde çalışan özel bir MCP sunucusunu Copilot Agent ile kullanmak istemektedir.

Bu durumda geliştiricinin karşılaşacağı durum ve yapılması gereken işlem nedir?

A) Yerel sunucular izin listelerinden muaftır, doğrudan çalışır.  
B) Yerel sunucu engellenir; geliştiricinin bunu kullanabilmesi için söz konusu yerel MCP sunucusunun kurumsal MCP Registry içinde listelenmesi ve Sunucu Kimliğinin (Server ID) birebir eşleşmesi gerekir.  
C) Geliştirici yerel makinedeki Windows güvenlik duvarını kapatmalıdır.  
D) "Registry only" modunda yerel sunucuların kullanımı teknik olarak tamamen imkansızdır, hiçbir şekilde izin verilemez.  

> **Doğru Cevap:** **B**  
> **Açıklama:** "Registry only" modunda yerel (local) MCP sunucuları dahi kayıt defterinde tam eşleşen ID ile tanımlı olmak zorundadır. Aksi halde istemci bağlantıyı reddeder.

---

### Soru 22 (Tek Seçim - GitHub Agentic Workflows / gh-aw)
GitHub Agentic Workflows (`gh-aw`) mimarisinde iş akışının yapısı nasıldır?

A) Yalnızca C# ile yazılmış binary dosyalardır.  
B) YAML frontmatter (tetikleyiciler, izinler, safe-outputs, tools) ve Markdown gövdesi (doğal dilde tanımlanan iş niyeti) içerir; derlenerek bir lock file oluşturur.  
C) Geleneksel Jenkins pipeline betikleridir.  
D) LLM modellerinin kaynak kodunu barındıran depolardır.  

> **Doğru Cevap:** **B**  
> **Açıklama:** GitHub Agentic Workflows, frontmatter ile korkulukları ve izinleri belirler; Markdown ile amacı doğal dilde anlatır ve GitHub Actions üzerinde çalıştırılmak üzere derlenmiş bir lock dosyası üretir.

---

### Soru 23 (Tek Seçim - Safe Outputs)
GitHub Agentic Workflows içinde yer alan **safe-outputs** özelliğinin temel güvenlik işlevi nedir?

A) Ajanın doğrudan depoya kontrolsüz yazma işlemi yapmasını engeller; ajan yalnızca bir çıktı önerir, onaylanmış ayrı bir güvenli adım bu çıktıyı kontrollü şekilde uygular.  
B) Veritabanı yedeklerini harici diske kopyalar.  
C) Ajanın ekran görüntüsü almasını sağlar.  
D) Runner üzerindeki tüm ortam değişkenlerini siler.  

> **Doğru Cevap:** **A**  
> **Açıklama:** Safe-outputs, "reasoning" (akıl yürütme) ile "execution" (yürütme) arasındaki sınır kapısıdır. Ajan içeriği üretir, ancak write yetkisine sahip ayrı bir gated step bu çıktıyı güvenlik taramasından geçirerek uygular.

---

### Soru 24 (Tek Seçim - Özel Ajan Tanımları)
Bir depoda `.github/agents/security-reviewer.agent.md` dosyası oluşturulmuştur. Dosya içeriği şöyledir:

```yaml
---
applyTo:
  - '**/*.js'
  - 'src/auth/**'
tools:
  - read_file
  - search_files
---
```

Bu özel ajan (custom agent) hakkında aşağıdakilerden hangisi **doğrudur**?

A) Bu ajan yeni bir git dalı oluşturma ve otomatik PR açma yetkisine sahiptir.  
B) Ajan yalnızca JS ve `src/auth/` dosyalarına odaklanacak ve yalnızca dosya okuma/arama araçlarını kullanabilecektir; dal oluşturma ve PR davranışları ise ajanın kendisi tarafından değil, onu yürüten sistem tarafından belirlenir.  
C) Ajan depodaki tüm dosyaları silebilir.  
D) `applyTo` alanı ajanın yetkisini değil, GitHub Actions runner işletim sistemini belirler.  

> **Doğru Cevap:** **B**  
> **Açıklama:** Özel ajanlar `applyTo` ile dosya kapsamını, `tools` ile araç yetkisini sınırlar. Ancak dal oluşturma veya PR açma gibi yürütme sınırları ajanın dosyasından değil, yürütme bağlamından (platform/orchestrator) kontrol edilir.

---

### Soru 25 (Tek Seçim - GITHUB_TOKEN İzinleri)
Bir ajan yalnızca bir PR üzerinde analiz yapacak ve inceleme yorumu ekleyecektir; ancak kaynak kodlara yeni commit atmayacaktır.

En düşük yetki ilkesine (least privilege) göre iş akışında hangi izin tanımlanmalıdır?

A)
```yaml
permissions: write-all
```
B)
```yaml
permissions:
  contents: read
  pull-requests: write
```
C)
```yaml
permissions:
  contents: write
  pull-requests: none
```
D)
```yaml
permissions: none
```

> **Doğru Cevap:** **B**  
> **Açıklama:** PR'a yorum yazmak ve inceleme durumunu güncellemek için `pull-requests: write`, repo içeriğini okumak içinse `contents: read` yeterlidir. `contents: write` izni verilmemelidir.

---

### Soru 26 (Tek Seçim - Runner Üzerinde Copilot CLI Çağrısı)
Bir CI iş akışı adımında Copilot CLI kullanılarak otomatik özetleme yaptırılacaktır. Kullanıcı etkileşiminin beklenmemesi ve kimlik doğrulamasının sağlanması için adım nasıl yapılandırılmalıdır?

A) `run: copilot chat`  
B)
```yaml
env:
  COPILOT_GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: npx @github/copilot-cli -p "Summarize changes" --no-ask-user
```
C) `run: git push origin main --force`  
D) `run: ssh root@copilot-server`  

> **Doğru Cevap:** **B**  
> **Açıklama:** Non-interactive CI ortamında `--no-ask-user` bayrağı ile prompt gönderilir ve `COPILOT_GITHUB_TOKEN` ortam değişkeni üzerinden token enjekte edilir.

---

### Soru 27 (Tek Seçim - Çoklu Ajan Çakışmalarını Önleme)
Aynı depoda hem bir bağımlılık güncelleme ajanı (Dependency Agent) hem de bir yeniden düzenleme ajanı (Refactoring Agent) çalışmaktadır.

Bu iki ajanın sürekli çakışan PR'lar üretmesini engellemek için mimari olarak yapılması gereken en temel işlem nedir?

A) Ajanların her ikisine de tüm repoda tam yazma yetkisi vermek  
B) Kapsam sınırları (scope boundaries) tanımlamak: Dependency ajanını sadece manifest ve lockfile dosyalarıyla, Refactoring ajanını ise sadece `src/` altındaki kodlarla sınırlandırmak  
C) Ajanları aynı dal (branch) üzerinde sırayla çalıştırmak  
D) PR incelemelerini devre dışı bırakmak  

> **Doğru Cevap:** **B**  
> **Açıklama:** Çoklu ajan mimarisinde istikrar, kapsam sınırlarının (scope boundaries) net çizilmesiyle başlar. Ajanların dokunduğu dosya yolları ayrıştırıldığında gereksiz çakışmalar önlenir.

---

### Soru 28 (Tek Seçim - Fan-Out / Fan-In Orkestrasyonu)
Aşağıdaki iş akışı konfigürasyonunu inceleyiniz:

```yaml
jobs:
  spec_analyzer:
    runs-on: ubuntu-latest
    steps: [...]

  risk_reviewer:
    runs-on: ubuntu-latest
    steps: [...]

  plan_merger:
    runs-on: ubuntu-latest
    needs: [spec_analyzer, risk_reviewer]
    steps: [...]
```

Bu yapı hangi orkestrasyon modelini temsil eder ve `plan_merger` ne zaman çalışır?

A) Sequential Pipeline; `plan_merger` yalnızca `spec_analyzer` tamamlandığında çalışır.  
B) Fan-Out / Fan-In Pattern; `spec_analyzer` ve `risk_reviewer` paralel çalışır (fan-out), `plan_merger` ise her iki iş de başarıyla tamamlandığında birleştirme yapmak üzere devreye girer (fan-in).  
C) Matrix Strategy; tüm işler sonsuz döngüde çalışır.  
D) Direct Push Pattern; işler arasında bağımlılık yoktur.  

> **Doğru Cevap:** **B**  
> **Açıklama:** `needs: [jobA, jobB]` yapısı klasik Fan-In orkestrasyonudur. Bağımsız analizler paralel yürütülür, ardından sonuçlar tek bir birleştirici işte toplanır.

---

### Soru 29 (Tek Seçim - Workflow-Level Concurrency Yapılandırması)
Bir depoda bir ajan sık sık aynı PR dalına yeni commit'ler göndermektedir. Önceki iş akışlarının iptal edilerek en güncel commit için çalışması, ancak **farklı iş akışlarının birbirini engellememesi** istenmektedir.

Hangi concurrency yapılandırması kullanılmalıdır?

A)
```yaml
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: false
```
B)
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
C)
```yaml
concurrency:
  group: global
  cancel-in-progress: true
```
D)
```yaml
concurrency:
  group: ${{ github.actor }}
```

> **Doğru Cevap:** **B**  
> **Açıklama:** `group: ${{ github.workflow }}-${{ github.ref }}` ifadesi, eşzamanlılığı hem iş akışı hem de dal bazında izole eder. Sadece `${{ github.ref }}` kullanılırsa aynı daldaki ilgisiz iş akışları da birbirini iptal edebilir. `cancel-in-progress: true` ise eski çalıştırmayı sonlandırır.

---

### Soru 30 (Tek Seçim - Copilot Ajan Modları Paralellik Kapasitesi)
Bir DevOps mühendisi, birden fazla bağımsız ajan oturumunu aynı anda paralel olarak çalıştırmak istemektedir.

Aşağıdaki Copilot çalışma modlarından hangisi **birden fazla paralel oturumu desteklemez (yalnızca sıralı / serial çalışır)**?

A) Copilot Cloud  
B) Copilot CLI  
C) Copilot Local (IDE Agent Mode)  
D) GitHub Agentic Workflows  

> **Doğru Cevap:** **C**  
> **Açıklama:** GH-600 müfredatındaki "Copilot Agent Modes: Parallelism Capabilities" tablosuna göre: Copilot Cloud ve Copilot CLI paralel oturumları desteklerken, Local (IDE) modu paralel oturumları desteklemez; yalnızca sıralı (serial - tek tek) çalışabilir.

---

### Soru 31 (Tek Seçim - Tahkim ve Eskalasyon Eşiği)
İki farklı ajan, aynı güvenlik uyarısını çözmek için birbirleriyle çelişen iki ayrı Pull Request açmıştır. Ajanlar PR'larını rebase etmeye çalışmış fakat her iki PR da üst üste iki kez çakışma hatası vermiştir.

GH-600 operasyonel kurallarına göre bu aşamada sistem nasıl davranmalıdır?

A) Ajanlar sonsuza kadar rebase denemeye devam etmelidir.  
B) İlk rebase atan ajanın PR'ı otomatik merge edilmeli, diğeri silinmelidir.  
C) Otomasyon durdurulmalı; neyin çakıştığını, nelerin denendiğini ve olası seçenekleri özetleyen bir raporla insan inceleyicisine eskalasyon yapılmalıdır.  
D) Her iki PR da kalıcı olarak silinmeli ve repo kilitlenmelidir.  

> **Doğru Cevap:** **C**  
> **Açıklama:** İstikrarlı sistemlerde eskalasyon kuralı: Aynı hata veya çakışma 2 kez tekrarlandığında otomatik deneme durdurulur ve insana yapılandırılmış kanıtlarla eskalasyon yapılır. "İlk merge olan kazanır" yaklaşımı anti-pattern'dir.

---

### Soru 32 (Tek Seçim - Subagents ve Handoff Sözdizimi)
Bir planlama ajanı (`planner.agent.md`), işini bitirdikten sonra görevi otomatik olarak `implementer` adlı alt ajana devretmek istemektedir.

`.agent.md` YAML frontmatter içinde bu geçiş nasıl yapılandırılmalıdır?

A)
```yaml
---
agents: [implementer]
handoffs:
  - label: Start Implementation
    agent: implementer
    send: true
---
```
B)
```yaml
---
tools: [implementer]
auto-run: true
---
```
C)
```yaml
---
subagents-all: true
---
```
D)
```yaml
---
forward-to: implementer.exe
---
```

> **Doğru Cevap:** **A**  
> **Açıklama:** Ajan dosyasında `agents:` listesinde izin verilen alt ajan belirtilir ve `handoffs:` bloğu altında ilgili ajana geçiş ve otomatik gönderme (`send: true`) tanımlanır.

---

### Soru 33 (Tek Seçim - Canlı Oturum İzleme CLI)
Takımınızda çalışan uzun süreli bir GitHub Copilot bulut ajan görevinin takıldığından şüpheleniyorsunuz.

Ajanın çalışma anındaki canlı log akışını terminalden gerçek zamanlı izlemek için hangi GitHub CLI komutu kullanılır?

A) `gh run list --all`  
B) `gh agent-task view --log --follow`  
C) `gh pr checks --watch`  
D) `gh copilot status --debug`  

> **Doğru Cevap:** **B**  
> **Açıklama:** Dokümantasyonda belirtildiği üzere canlı oturum loglarını canlı izlemek (live-stream) için `gh agent-task view --log --follow` komutu kullanılır.

---

### Soru 34 (Tek Seçim - Ruleset Bypass Aktörü)
Reponuzda tüm dallara push edilen commit'lerin GPG ile imzalanmış olmasını zorunlu kılan bir Ruleset bulunmaktadır. Ancak GitHub Copilot kodlama ajanı commit'leri kriptografik olarak imzalayamadığı için `copilot/*` dalına push yaparken hata almaktadır.

İnsanlar için imzalama kuralını korurken ajanın çalışabilmesini sağlamak için ne yapılmalıdır?

A) İmzalı commit zorunluluğu kuralı tüm repoda tamamen silinmelidir.  
B) Deponun Ruleset ayarlarında "GitHub Copilot" ilgili kural için bir bypass aktörü (bypass actor) olarak eklenmelidir.  
C) Ajanın her commit'i için sahte bir imza üretilmelidir.  
D) Ajanın doğrudan `main` dalına push yapmasına izin verilmelidir.  

> **Doğru Cevap:** **B**  
> **Açıklama:** Kurumsal repository ruleset'lerinde "GitHub Copilot", belirli kurallar (örneğin signed commits) için bypass aktörü olarak tanımlanabilir. Bu sayede otomasyon dalları engellenmezken insan katkıcılar denetlenmeye devam eder.

---

### Soru 35 (Tek Seçim - disable-model-invocation Ayarı)
Bir ajanın ön yüzünde (frontmatter) `disable-model-invocation: true` değeri tanımlanmıştır.

Bu ayarın ajan davranışı üzerindeki doğrudan etkisi nedir?

A) Ajanın hiçbir araç kullanmasına izin verilmez.  
B) Ajan başka bir ana ajan tarafından orkestrasyon sırasında alt ajan (subagent) olarak çağrılamaz.  
C) Ajan web arayüzünde kullanıcılara görünmez.  
D) Ajan yalnızca geceleri çalıştırılabilir.  

> **Doğru Cevap:** **B**  
> **Açıklama:** `disable-model-invocation: true`, ajanın model tabanlı orkestrasyonlar tarafından bir alt ajan olarak çağrılmasını kilitler. Kullanıcı arayüzünde gizlemek için ise `user-invocable: false` kullanılır.

---

### Soru 36 (Tek Seçim - Bellek Hiyerarşisi: Source of Truth)
Ajanik sistemlerde üç temel bellek türü bulunur: Kısa Vadeli, Uzun Vadeli ve Harici Bellek.

Bir görevin kabul kriterleri, gereksinimleri ve değişmez kuralları için **en güvenilir "Source of Truth" (Doğruluk Kaynağı)** olarak kabul edilen bellek katmanı ve GitHub karşılığı hangisidir?

A) Kısa vadeli bellek - Modelin o anki prompt geçmişi  
B) Harici bellek - GitHub Issue ve Pull Request açıklamaları gibi kalıcı depo yapıtları  
C) Uzun vadeli bellek - Tarayıcı çerezleri  
D) Harici bellek - Geçici Actions runner konsol logları  

> **Doğru Cevap:** **B**  
> **Açıklama:** Harici bellek (External memory), oturumlardan bağımsız yaşayan, denetlenebilir ve kalıcı GitHub nesneleridir (Issues, PRs, instructions). Gereksinimler issue'da, kararlar PR'da tutulur ve asıl kaynak burasıdır.

---

### Soru 37 (Tek Seçim - Bağlam Kayması / Context Drift)
Ajanik bir iş akışında "Context Drift" (Bağlam Kayması) kavramı neyi ifade eder?

A) Runner'ın internet bağlantısının anlık olarak kopmasını  
B) Ajanın yaptığı değişikliklerin zamanla orijinal görev hedefinden, kabul kriterlerinden veya önceki mimari kararlardan sapması durumunu  
C) 90 gün sonra Actions loglarının silinmesini  
D) Ajanın Python yerine JavaScript kodu yazmasını  

> **Doğru Cevap:** **B**  
> **Açıklama:** Context drift, ajanın uzun süren veya çok adımlı görevlerde asıl hedeften uzaklaşarak gereksiz ya da çelişkili değişiklikler üretmeye başlamasıdır.

---

### Soru 38 (Tek Seçim - Context Drift'i Düzeltme)
Bir ajan üzerinde çalıştığı PR'da context drift yaşamış ve issue'da istenmeyen alakasız dosyaları değiştirmeye başlamıştır.

Ajanı doğru yola sokmak için uygulanması gereken en doğru yöntem nedir?

A) Ajanın hafızasını tazelemek için tüm repoyu silip baştan klonlamak  
B) Ajanı "Source of Truth" olan ana Issue ve PR kabul kriterlerine yeniden çıpalamak (re-anchor), gerekirse PR açıklamasını netleştirip alakasız commit'leri geri almak  
C) Ajanı bekletmeden PR'ı mevcut haliyle onaylayıp birleştirmek  
D) Runner'a daha fazla RAM vermek  

> **Doğru Cevap:** **B**  
> **Açıklama:** Context drift düzeltilirken ajan oturumdaki sohbet geçmişine değil, asıl kaynak olan Issue ve PR kabul kriterlerine yeniden çıpalanır (re-anchor to source of truth).

---

### Soru 39 (Tek Seçim - Actions Saklama Süreleri / Retention Policies)
GitHub Actions tarafından üretilen iş akışı logları ve yüklenen artifact'lar varsayılan olarak kaç gün saklanır?

A) 7 gün  
B) 30 gün  
C) 90 gün  
D) 365 gün  

> **Doğru Cevap:** **C**  
> **Açıklama:** GitHub Actions varsayılan olarak log ve artifact'ları 90 gün saklar ve süre dolduğunda otomatik olarak kalıcı olarak siler.

---

### Soru 40 (Tek Seçim - Private Repolarda Maksimum Saklama Süresi)
Bir kurum denetim ve uyumluluk (compliance) gereği özel (private) depolarında GitHub Actions artifact saklama süresini uzatmak istemektedir.

GitHub politikalarına göre özel bir depoda artifact saklama süresi en fazla kaç güne kadar yapılandırılabilir?

A) 90 gün  
B) 180 gün  
C) 400 gün  
D) Sınırsız (unlimited)  

> **Doğru Cevap:** **C**  
> **Açıklama:** Public repolarda saklama süresi 1-90 gün arasındayken, private depolarda bu süre 400 güne kadar yapılandırılabilir.

---

### Soru 41 (Tek Seçim - Artifact Silinmesini Denetleme)
Bir adli bilişim (forensic) incelemesi sırasında, bir ajana ait kritik bir doğrulama artifact'ının beklenenden önce ortadan kaybolduğu fark edilmiştir.

Bu dosyanın bir kullanıcı veya işlem tarafından silinip silinmediğini doğrulamak için GitHub Organization Audit Log'unda hangi olay (event) aranmalıdır?

A) `action:file.remove`  
B) `action:artifact.destroy`  
C) `workflow.clean`  
D) `git.branch.delete`  

> **Doğru Cevap:** **B**  
> **Açıklama:** GH-600 dokümantasyonunda açıkça belirtildiği üzere, artifact silinme olayları kurumsal denetim günlüğünde `action:artifact.destroy` adı altında kaydedilir.

---

### Soru 42 (Tek Seçim - Kök Neden Sınıflandırması)
Bir ajan kendisine verilen görevde `npm run test` komutu yerine yanlış parametrelerle geçersiz bir script çalıştırmış ve iş akışı bu sebeple kırılmıştır.

Bu hata türü GH-600 hata sınıflandırma modeline göre hangi kategoriye girer?

A) Reasoning error (Muhakeme hatası)  
B) Tool misuse (Araç kötüye kullanımı / yanlış kullanımı)  
C) Context issue (Bağlam sorunu)  
D) Hardware failure (Donanım arızası)  

> **Doğru Cevap:** **B**  
> **Açıklama:** Komutların, betiklerin, repo işlemlerinin veya araçların yanlış argümanlarla ya da yanlış sırada çağrılması "Tool misuse" olarak sınıflandırılır.

---

### Soru 43 (Tek Seçim - Oturumlar Arası Durum Sürekliliği)
Bir geliştirici, ajanla çalışmaya VS Code IDE ortamında başlamış, ardından görevi terminaldeki Copilot CLI üzerinden devam ettirmiş ve son doğrulamayı GitHub web üzerinde tamamlamıştır.

Farklı ortamlar arasında durum sürekliliğini (continuity) sağlayan ve kayıpları önleyen temel unsur nedir?

A) Geliştiricinin chat geçmişini kopyalayıp metin belgesine yapıştırması  
B) Tüm araçların ortak bir durum çapası (state anchor) olarak aynı Pull Request numarasına, branch adına ve commit SHA değerlerine dayanması  
C) Geliştiricinin bilgisayarını hiç kapatmaması  
D) Her ortam geçişinde ajanın tüm kodu sıfırdan yazması  

> **Doğru Cevap:** **B**  
> **Açıklama:** Süreklilik, geçici oturum verilerinin taşınmasıyla değil; PR numarası, dal adı, commit SHA gibi kalıcı GitHub referanslarına dayanarak sağlanır.

---

### Soru 44 (Tek Seçim - Risk Tabanlı Otonomi Düzeyleri)
Bir ajan altyapı kodlarında (`infra/terraform`) kritik bir veritabanı ayarını değiştirecektir.

Risk tabanlı otonomi modeline göre bu eylem için uygulanması gereken en uygun yönetişim düzeyi hangisidir?

A) Full Automation: Testler geçerse doğrudan otomatik merge ve deploy edilmelidir.  
B) Read-only Autonomy: Ajan hiçbir plan dahi üretememelidir.  
C) Human-Authorized Execution / Environment Approval Gate: Ajan yalnızca planı ve PR'ı hazırlamalı; üretim ortamı dağıtımı ve secret erişimi kesinlikle yetkili bir insanın açık onayına (approval gate) bağlı olmalıdır.  
D) Unbounded Autonomy: Ajan kararı tek başına vermelidir.  

> **Doğru Cevap:** **C**  
> **Açıklama:** Altyapı ve prodüksiyon değişiklikleri "Critical/High Risk" kategorisindedir. Ajan işi hazırlayabilir ancak çalıştırma yetkisi Environments onay kapılarıyla insanda tutulmalıdır.

---

### Soru 45 (Tek Seçim - Terminal Ajanı Araç Sınırlandırması)
Geliştiricilerden biri, Copilot CLI ajanını kullanarak son 10 commit'i özetlemek ve olası kırıcı değişiklikleri (breaking changes) listelemek istemektedir. Ancak ajana depoda değişiklik yapma veya rastgele komut çalıştırma yetkisi vermek istememektedir.

En düşük yetki ilkesine uygun doğru CLI komutu hangisidir?

A) `copilot -p "Summarize commits" --allow-all-tools`  
B) `copilot -p "Summarize the last 10 commits and highlight breaking changes." --allow-tool 'shell(git)'`  
C) `copilot -p "Summarize commits" --sudo`  
D) `copilot -p "Summarize commits" --write-to-main`  

> **Doğru Cevap:** **B**  
> **Açıklama:** Yalnızca salt-okunur git incelemesi yapılması gerektiğinde `--allow-tool 'shell(git)'` parametresi ile ajanın yetki alanı sadece git komutlarıyla sınırlandırılır.

---

### Soru 46 (Tek Seçim - Bot PR Guardrail İş Akışı)
Kurumunuzda hiçbir ajan tarafından açılan Pull Request'in yalnızca botların (örneğin başka otomasyonların) onayıyla birleştirilmemesi istenmektedir. Her ajan PR'ında en az bir gerçek insan kullanıcı onayı bulunması şart koşulmuştur.

Bunu GitHub Actions üzerinde zorunlu kılmak için hangi yaklaşım uygulanmalıdır?

A) Depodaki tüm bot hesaplarının silinmesi  
B) PR'da `github-copilot[bot]` tarafından açılan PR'ları denetleyen ve `actions/github-script` kullanarak incelemeciler arasında `user.type === "User"` ve `user.login !== "github-copilot[bot]"` olan en az bir onaylanmış inceleme (APPROVED) arayan bir guardrail iş akışı yazıp bunu Required Status Check yapmak  
C) GitHub Actions kullanımını tamamen durdurmak  
D) PR başlığına "[Human Approved]" yazılmasını istemek  

> **Doğru Cevap:** **B**  
> **Açıklama:** Dokümantasyonda verilen defense-in-depth örneğinde, `actions/github-script` PR incelemelerini listeleyerek onay veren aktörün `User` tipinde ve bot olmadığını doğrular, aksi halde iş akışını başarısız (`core.setFailed`) kılar.

---

### Soru 47 (Tek Seçim - PreToolUse Hook Şeması)
Aşağıdaki `.github/hooks/guardrails.json` kuralını inceleyiniz:

```json
{
  "hook": "preToolUse",
  "tools": ["shell(bash)"],
  "rules": [
    { "match": "sudo", "permissionDecision": "deny" },
    { "match": "rm -rf /", "permissionDecision": "deny" }
  ]
}
```

Ajan terminalde `sudo apt-get install jq` komutunu çalıştırmayı denediğinde ne gerçekleşir?

A) Komut arka planda sessizce çalıştırılır.  
B) Hook komut içerisindeki `sudo` ifadesini yakalar, yürütülmesini engeller (`permissionDecision: deny`) ve hata üreterek insana eskalasyon tetikler.  
C) Bilgisayar kendini yeniden başlatır.  
D) Kural yalnızca uyarı logu basar fakat komutun çalışmasına izin verir.  

> **Doğru Cevap:** **B**  
> **Açıklama:** `preToolUse` hook kuralları eşleşme olduğunda eylemi çalıştırmadan önce engeller. Bu sayede modelin kararından bağımsız teknik bir bariyer oluşturulur.

---

### Soru 48 (Tek Seçim - Yönetişim Rutinleri / Governance Cadence)
Ajanik sistemlerin operasyonel yönetişim döngüsünde (Governance Cadence), **"GITHUB_TOKEN izinlerinin ve ortam bazlı gizli anahtar (secrets) kapsamlarının gözden geçirilmesi"** hangi periyotta yapılması önerilen bir kontroldür?

A) Günlük (Daily)  
B) Haftalık (Weekly)  
C) Aylık (Monthly)  
D) Yılda bir (Annually)  

> **Doğru Cevap:** **C**  
> **Açıklama:** GH-600 standartlarına göre:
> - Haftalık (Weekly): Başarısız çalıştırmalar ve politika ihlalleri.
> - Aylık (Monthly): Workflow izinleri ve secrets kapsamları.
> - Üç Aylık (Quarterly): Ruleset'ler, CODEOWNERS ve saklama politikaları.

---

### Soru 49 (Tek Seçim - Rubber-Stamping Anti-Pattern)
Geliştiricilerin, ajanlar tarafından açılan PR'larda testlerin yeşil olduğunu gördükten sonra değişikliklerin içeriğini, kapsamını ve güvenlik etkilerini okumadan doğrudan "Approve" butonuna basarak birleştirmesi hangi yönetimsel arızayı (anti-pattern) ifade eder?

A) Unbounded autonomy  
B) Rubber-stamping (Körlemesine Onaylama)  
C) Missing audit trail  
D) Bypass paths exist  

> **Doğru Cevap:** **B**  
> **Açıklama:** "Rubber-stamping", incelemecilerin otomasyona aşırı güvenerek veya yorularak (governance fatigue) kontrol etmeden onay vermesidir. Bunu engellemek için PR boyutları küçük tutulmalı ve kanıtlar net sunulmalıdır.

---

### Soru 50 (Tek Seçim - En Düşük Yetkili İş Akışı Mimarisi)
Bir iş akışı iki işten oluşmaktadır:
1. `audit_repo`: Depoyu tarar ve güvenlik raporu üretir.
2. `publish_alert`: Rapor sonucuna göre depoda bir Issue açar.

En düşük yetki (least privilege) prensibine göre bu iş akışının izinleri (permissions) nasıl yapılandırılmalıdır?

A)
```yaml
permissions: write-all
```
B)
```yaml
permissions:
  contents: read

jobs:
  audit_repo:
    runs-on: ubuntu-latest
    steps: [...]

  publish_alert:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps: [...]
```
C)
```yaml
permissions: none
```
D)
```yaml
permissions:
  issues: write
```

> **Doğru Cevap:** **B**  
> **Açıklama:** İş akışı düzeyinde varsayılan olarak en kısıtlı izin (`contents: read`) tanımlanmalı, yazma yetkisi (`issues: write`) yalnızca yazma işlemini yapacak olan `publish_alert` işine (job-level) verilmelidir. Bu sayede `audit_repo` işinin kaza veya enjeksiyon anında issue veya koda yazması engellenir.

---
*Başarılar! Bu 50 soruyu ve arkasındaki mantığı tam olarak kavramak GH-600 sertifika sınavında karşınıza çıkacak senaryoları eksiksiz yanıtlamanızı sağlayacaktır.*
