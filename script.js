/**
 * WEDDING INVITATION INTERACTIVE SCRIPTS: SANRO & FITRA
 * Ultra-Luxury Obsidian & Champagne Gold Edition
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const coverScreen = document.getElementById('cover-screen');
  const btnOpenInvitation = document.getElementById('btn-open-invitation');
  const bgMusic = document.getElementById('bg-music');
  const musicToggleBtn = document.getElementById('music-toggle-btn');
  const musicIcon = document.getElementById('music-icon');
  const guestNameCover = document.getElementById('guest-name-cover');
  const wishesNameInput = document.getElementById('wishes-name');
  const toastNotice = document.getElementById('toast-notice');
  const toastMessage = document.getElementById('toast-message');

  let isMusicPlaying = false;

  // 1. Dynamic Guest Name from URL parameter (?to=Bapak+Joko or ?guest=Nama or ?nama=Nama)
  const urlParams = new URLSearchParams(window.location.search);
  const guestParam = urlParams.get('to') || urlParams.get('guest') || urlParams.get('nama');
  if (guestParam) {
    const formattedGuest = decodeURIComponent(guestParam).trim();
    if (formattedGuest) {
      if (guestNameCover) guestNameCover.textContent = formattedGuest;
      if (wishesNameInput) wishesNameInput.value = formattedGuest;
    }
  }

  // 2. Open Invitation Action
  if (btnOpenInvitation) {
    btnOpenInvitation.addEventListener('click', () => {
      // Unlock body scroll
      document.body.classList.remove('lock-scroll');

      // Animate cover out
      coverScreen.classList.add('opened');

      // Play music
      playAudio();

      // Smooth scroll to top of content
      setTimeout(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }, 250);
    });
  }

  // 3. Audio Controls
  function playAudio() {
    if (!bgMusic) return;
    bgMusic.play().then(() => {
      isMusicPlaying = true;
      musicToggleBtn.classList.add('rotating');
      musicIcon.className = 'fa-solid fa-compact-disc';
    }).catch(err => {
      console.log('Audio autoplay prevented or file loading:', err);
      isMusicPlaying = false;
    });
  }

  function pauseAudio() {
    if (!bgMusic) return;
    bgMusic.pause();
    isMusicPlaying = false;
    musicToggleBtn.classList.remove('rotating');
    musicIcon.className = 'fa-solid fa-volume-xmark';
  }

  if (musicToggleBtn) {
    musicToggleBtn.addEventListener('click', () => {
      if (isMusicPlaying) {
        pauseAudio();
        showToast('Musik dijeda');
      } else {
        playAudio();
        showToast('Musik diputar');
      }
    });
  }

  // 4. Countdown Timer (21 Oktober 2026 10:00:00 WIB / UTC+7)
  const weddingDate = new Date('2026-10-21T10:00:00+07:00').getTime();

  function updateCountdown() {
    const now = new Date().getTime();
    const distance = weddingDate - now;

    const daysEl = document.getElementById('count-days');
    const hoursEl = document.getElementById('count-hours');
    const minutesEl = document.getElementById('count-minutes');
    const secondsEl = document.getElementById('count-seconds');

    if (distance < 0) {
      if (daysEl) daysEl.textContent = '00';
      if (hoursEl) hoursEl.textContent = '00';
      if (minutesEl) minutesEl.textContent = '00';
      if (secondsEl) secondsEl.textContent = '00';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
    if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
    if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
    if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);

  // 5. Toast Notification Utility
  window.showToast = function (message) {
    if (!toastNotice || !toastMessage) return;
    toastMessage.textContent = message;
    toastNotice.classList.add('show');
    clearTimeout(window.toastTimer);
    window.toastTimer = setTimeout(() => {
      toastNotice.classList.remove('show');
    }, 3200);
  };

  // 6. Copy Account Number
  window.copyAccountNumber = function (accountNumber) {
    navigator.clipboard.writeText(accountNumber).then(() => {
      showToast('Nomor rekening BRI berhasil disalin!');
    }).catch(() => {
      const tempInput = document.createElement('input');
      tempInput.value = accountNumber;
      document.body.appendChild(tempInput);
      tempInput.select();
      document.execCommand('copy');
      document.body.removeChild(tempInput);
      showToast('Nomor rekening BRI berhasil disalin!');
    });
  };

  // 7. Google Firebase Realtime Database & LocalStorage Dual-Mode
  // ========================================================
  // Tempelkan konfigurasi Firebase dari console.firebase.google.com:
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "firebase/app";
  import { getAnalytics } from "firebase/analytics";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyCvP4JOb_Sq66VZlFBu0IGwmOKF4U2rHBU",
    authDomain: "wedding-sanro-fitra.firebaseapp.com",
    databaseURL: "https://wedding-sanro-fitra-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "wedding-sanro-fitra",
    storageBucket: "wedding-sanro-fitra.firebasestorage.app",
    messagingSenderId: "78885276376",
    appId: "1:78885276376:web:7a6305d7f8ee2cc62aa5ad",
    measurementId: "G-WG5WBY1TSH"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
  // ========================================================

  let firebaseDb = null;
  let wishesRef = null;

  if (window.firebase && firebaseConfig.apiKey && firebaseConfig.databaseURL) {
    try {
      if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
      }
      firebaseDb = firebase.database();
      wishesRef = firebaseDb.ref('wedding_wishes');
      console.log('Firebase Realtime Database connected!');
    } catch (e) {
      console.warn('Firebase initialization error:', e);
    }
  }

  const defaultWishes = [];

  function getStoredWishes() {
    try {
      const stored = localStorage.getItem('wedding_sanro_fitra_prayers');
      if (stored) {
        const parsed = JSON.parse(stored);
        // Hapus data contoh lama jika tersimpan di cache browser
        const filtered = parsed.filter(p => !['St. P. Sitanggang & Kel.', 'Keluarga Besar Sinurat', 'Rekan Muda-Mudi Stasi Pispis'].includes(p.name));
        return filtered;
      }
      return [];
    } catch (e) {
      return [];
    }
  }

  function saveWishes(wishes) {
    try {
      localStorage.setItem('wedding_sanro_fitra_prayers', JSON.stringify(wishes));
    } catch (e) {
      console.error(e);
    }
  }

  function loadWishes() {
    if (wishesRef) {
      wishesRef.limitToLast(100).on('value', (snapshot) => {
        const data = [];
        snapshot.forEach(child => {
          const val = child.val();
          data.unshift({
            name: val.name,
            relation: val.relation,
            message: val.message,
            time: formatTimeAgo(val.timestamp || val.createdAt)
          });
        });
        renderList(data);
      }, (err) => {
        console.warn('Firebase fetch error, fallback to local:', err);
        renderList(getStoredWishes());
      });
      return;
    }
    renderList(getStoredWishes());
  }

  function formatTimeAgo(timestamp) {
    if (!timestamp) return 'Baru saja';
    try {
      const timeMs = typeof timestamp === 'number' ? timestamp : new Date(timestamp).getTime();
      const diffSec = Math.floor((Date.now() - timeMs) / 1000);
      if (diffSec < 60) return 'Baru saja';
      if (diffSec < 3600) return `${Math.floor(diffSec / 60)} menit lalu`;
      if (diffSec < 86400) return `${Math.floor(diffSec / 3600)} jam lalu`;
      return `${Math.floor(diffSec / 86400)} hari lalu`;
    } catch (e) {
      return 'Baru saja';
    }
  }

  function renderList(wishes) {
    const listContainer = document.getElementById('wishes-list');
    const totalCountEl = document.getElementById('total-wishes-count');
    if (!listContainer) return;

    const count = wishes ? wishes.length : 0;
    if (totalCountEl) totalCountEl.textContent = count;

    if (!wishes || wishes.length === 0) {
      listContainer.innerHTML = `
        <div class="text-center py-8 px-4 text-rose-200/70 font-sans text-xs">
          <div class="w-12 h-12 mx-auto mb-3 rounded-full bg-gold-400/10 border border-gold-400/30 flex items-center justify-center text-gold-400 text-lg shadow-inner">
            <i class="fa-regular fa-comment-dots"></i>
          </div>
          <p class="font-medium text-slate-200 mb-1">Belum ada untaian doa</p>
          <p class="text-[11px] text-rose-300/60 italic">Jadilah yang pertama menuliskan doa dan harapan terbaik untuk Sanro & Fitra.</p>
        </div>
      `;
      return;
    }

    listContainer.innerHTML = wishes.map(w => {
      const initial = w.name ? w.name.charAt(0).toUpperCase() : 'T';
      return `
        <div class="comment-item">
          <div class="flex items-start gap-3">
            <div class="avatar-circle flex-shrink-0">${initial}</div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between gap-2 flex-wrap">
                <h5 class="text-sm font-semibold text-white truncate">${escapeHtml(w.name)}</h5>
                ${w.relation ? `<span class="text-[10px] px-2 py-0.5 rounded-full border border-gold-400/30 text-gold-300 bg-gold-400/10">${escapeHtml(w.relation)}</span>` : ''}
              </div>
              <p class="text-xs text-rose-100 mt-2 leading-relaxed font-cormorant text-base">${escapeHtml(w.message)}</p>
              <span class="text-[10px] text-rose-300/60 block mt-2">${w.time || 'Baru saja'}</span>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  function escapeHtml(string) {
    return String(string).replace(/[&<>"'`=\/]/g, function (s) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '/': '&#x2F;',
        '=': '&#x3D;',
        '`': '&#x60;'
      }[s];
    });
  }

  loadWishes();

  // Handle Form Submit (Doa & Ucapan)
  const wishesForm = document.getElementById('wishes-form');
  if (wishesForm) {
    wishesForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const name = document.getElementById('wishes-name').value.trim();
      const relation = document.getElementById('wishes-relation')?.value.trim() || 'Kerabat / Tamu';
      const message = document.getElementById('wishes-message').value.trim();

      if (!name) {
        showToast('Mohon isi nama Anda');
        return;
      }
      if (!message) {
        showToast('Mohon tuliskan doa & ucapan restu Anda');
        return;
      }

      const newWish = {
        name: name,
        relation: relation,
        message: message,
        timestamp: Date.now(),
        time: 'Baru saja'
      };

      if (wishesRef) {
        try {
          await wishesRef.push({
            name: name,
            relation: relation,
            message: message,
            timestamp: Date.now()
          });
        } catch (err) {
          console.warn('Firebase push failed, saving locally:', err);
          const current = getStoredWishes();
          current.unshift(newWish);
          saveWishes(current);
          renderList(current);
        }
      } else {
        const current = getStoredWishes();
        current.unshift(newWish);
        saveWishes(current);
        renderList(current);
      }

      showToast('Terima kasih atas doa restu Anda!');
      document.getElementById('wishes-message').value = '';
    });
  }

  // 8. ScrollSpy for Bottom Navigation
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.bottom-nav .nav-item');

  function highlightNavOnScroll() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 160;
      const sectionId = current.getAttribute('id');

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navItems.forEach(item => {
          if (item.getAttribute('href') === `#${sectionId}`) {
            item.classList.add('active');
          } else {
            item.classList.remove('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', highlightNavOnScroll);
});
