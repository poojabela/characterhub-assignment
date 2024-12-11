<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import {
  Bars3Icon,
  UserIcon,
  MagnifyingGlassIcon,
  PlayIcon,
  HeartIcon,
  BookmarkIcon,
  ListBulletIcon,
  StarIcon,
} from '@heroicons/vue/24/outline'

import type { MovieDetails, CrewMember } from './types'

const movie = ref<MovieDetails | null>(null)
const isLoading = ref(true)

const fetchMovieDetails = async () => {
  try {
    const response = await fetch('https://www.omdbapi.com/?i=tt3896198&apikey=d2132124')
    const data = await response.json()
    movie.value = data
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchMovieDetails()
})

const crew = computed(() => {
  if (!movie.value) return []

  const crewMembers = []

  movie.value.Director.split(', ').forEach((director) => {
    crewMembers.push({
      name: director,
      role: 'Director',
    })
  })

  movie.value.Writer.split(', ').forEach((writer) => {
    const name = writer.split(' (')[0]
    crewMembers.push({
      name,
      role: 'Writer',
    })
  })

  return crewMembers
})
</script>

<template>
  <div class="min-h-screen bg-[#06142E] text-white">
    <header class="bg-[#032541] px-4 py-3 lg:hidden">
      <div class="flex items-center justify-between">
        <button>
          <Bars3Icon class="w-8 h-8" />
        </button>
        <div class="text-center">
          <span class="text-[#01b4e4] text-xl font-bold">TMDB</span>
        </div>
        <div class="flex items-center gap-4">
          <button>
            <UserIcon class="w-6 h-6" />
          </button>
          <button>
            <MagnifyingGlassIcon class="w-6 h-6" />
          </button>
        </div>
      </div>
    </header>

    <header class="hidden lg:block bg-[#032541] px-4 py-3">
      <div class="container mx-auto flex items-center justify-between">
        <div class="flex items-center space-x-8">
          <span class="text-[#01b4e4] text-2xl font-bold">TMDB</span>
          <nav class="flex space-x-6">
            <a href="#" class="text-white hover:text-[#01b4e4]">Movies</a>
            <a href="#" class="text-white hover:text-[#01b4e4]">TV Shows</a>
            <a href="#" class="text-white hover:text-[#01b4e4]">People</a>
            <a href="#" class="text-white hover:text-[#01b4e4]">More</a>
          </nav>
        </div>
        <div class="flex items-center space-x-4">
          <button class="px-3 py-1 bg-transparent border border-white rounded text-white">
            EN
          </button>
          <button class="text-white hover:text-[#01b4e4]">Login</button>
          <button class="text-white hover:text-[#01b4e4]">Join TMDB</button>
        </div>
      </div>
    </header>

    <!-- Navigation Tabs -->
    <nav class="bg-white border-b border-[#032541]">
      <div class="container mx-auto">
        <div class="flex text-[#032541] font-medium justify-center">
          <button class="px-2 py-1.5 border-b-2 border-[#01b4e4] md:px-4 md:py-3">
            Overview ▼
          </button>
          <button class="px-2 py-1.5 md:px-4 md:py-3">Media ▼</button>
          <button class="px-2 py-1.5 md:px-4 md:py-3">Fandom ▼</button>
          <button class="px-2 py-1.5 md:px-4 md:py-3">Share ▼</button>
        </div>
      </div>
    </nav>

    <main v-if="movie">
      <div class="hidden lg:block">
        <div class="relative min-h-[600px] bg-[#032541] overflow-hidden">
          <div class="absolute inset-0">
            <img
              :src="movie.Poster"
              alt="Background"
              class="w-full h-screen object-fill opacity-20"
            />
            <div class="absolute inset-0 bg-gradient-to-r"></div>
            <div
              class="absolute inset-0 bg-gradient-to-b from-[#032541]/0 via-[#032541]/80 to-[#032541]"
            ></div>
          </div>

          <!-- Content Container -->
          <div class="container mx-auto relative">
            <div class="flex gap-10 px-8 py-8">
              <!-- Left Column - Poster -->
              <div class="w-[300px] flex-shrink-0">
                <img :src="movie.Poster" :alt="movie.Title" class="w-full rounded-lg shadow-xl" />
                <div class="mt-4">
                  <button
                    class="flex items-center justify-center gap-2 w-full bg-[#032541] text-white py-3 px-4 rounded hover:bg-[#01b4e4] transition-colors"
                  >
                    <img alt="Disney+" class="w-6 h-6 rounded" />
                    <div class="text-center">
                      <div class="text-sm">Now Streaming</div>
                      <div class="font-bold">Watch Now</div>
                    </div>
                  </button>
                </div>
              </div>

              <!-- Right Column - Details -->
              <div class="flex-1 pt-4">
                <h1 class="text-4xl font-bold">
                  {{ movie.Title }}
                  <span class="text-white/60">({{ movie.Year }})</span>
                </h1>

                <div class="flex items-center gap-2 mt-4 text-base">
                  <span class="px-2 py-0.5 bg-[#032541]/50 rounded border border-white/20">{{
                    movie.Rated
                  }}</span>
                  <span>{{ movie.Released }} (KR)</span>
                  <span>•</span>
                  <span>{{ movie.Genre }}</span>
                  <span>•</span>
                  <span>{{ movie.Runtime }}</span>
                </div>

                <div class="flex items-center gap-6 mt-8">
                  <!-- Score Section -->
                  <div class="flex items-center gap-4">
                    <div class="relative w-16 h-16">
                      <div
                        class="absolute inset-0 rounded-full bg-[#081c22] flex items-center justify-center"
                      >
                        <span class="text-xl font-bold">76%</span>
                      </div>
                      <svg class="absolute inset-0" viewBox="0 0 36 36">
                        <path
                          d="M18 2.0845
                      a 15.9155 15.9155 0 0 1 0 31.831
                      a 15.9155 15.9155 0 0 1 0 -31.831"
                          fill="none"
                          stroke="#21d07a"
                          stroke-width="3"
                          stroke-dasharray="75, 100"
                        />
                      </svg>
                    </div>
                    <span class="font-semibold">User Score</span>
                  </div>

                  <!-- Emoji Reactions -->
                  <div class="flex items-center gap-2">
                    <span class="text-2xl">😍</span>
                    <span class="text-2xl">🤬</span>
                    <span class="text-2xl">🤣</span>
                  </div>

                  <!-- What's your vibe button -->
                  <button
                    class="px-4 py-1.5 bg-[#032541] rounded-full text-sm hover:bg-[#01b4e4] transition-colors"
                  >
                    What's your Vibe? ℹ️
                  </button>
                </div>

                <div class="flex items-center gap-4 mt-6">
                  <button
                    class="p-3 bg-[#032541] rounded-full hover:bg-[#01b4e4] transition-colors"
                  >
                    <ListBulletIcon class="w-5 h-5" />
                  </button>
                  <button
                    class="p-3 bg-[#032541] rounded-full hover:bg-[#01b4e4] transition-colors"
                  >
                    <HeartIcon class="w-5 h-5" />
                  </button>
                  <button
                    class="p-3 bg-[#032541] rounded-full hover:bg-[#01b4e4] transition-colors"
                  >
                    <BookmarkIcon class="w-5 h-5" />
                  </button>
                  <button
                    class="p-3 bg-[#032541] rounded-full hover:bg-[#01b4e4] transition-colors"
                  >
                    <StarIcon class="w-5 h-5" />
                  </button>
                  <button
                    class="flex items-center gap-2 px-4 py-2 bg-[#032541] rounded hover:bg-[#01b4e4] transition-colors"
                  >
                    <PlayIcon class="w-4 h-4" />
                    Play Trailer
                  </button>
                </div>

                <p class="mt-8 text-lg text-white/60 italic">Obviously.</p>

                <div class="mt-4">
                  <h2 class="text-2xl font-bold">Overview</h2>
                  <p class="mt-4 text-lg">{{ movie.Plot }}</p>
                </div>

                <div class="mt-8 grid grid-cols-3 gap-x-12 gap-y-6">
                  <div v-for="member in crew" :key="member.name" class="flex flex-col">
                    <span class="font-bold">{{ member.name }}</span>
                    <span class="text-sm text-white/60">{{ member.role }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Mobile Layout -->
      <div class="lg:hidden">
        <div class="relative w-full">
          <div class="relative w-full h-[300px] overflow-hidden">
            <img :src="movie.Poster" alt="Banner" class="w-full h-full object-fill opacity-100" />
            <div class="absolute inset-0 bg-gradient-to-b from-[#06142E]/10 to-[#06142E]"></div>
          </div>

          <div class="absolute left-4 top-[60px]">
            <div
              class="w-[120px] h-[180px] rounded-lg overflow-hidden shadow-lg border-2 border-[#032541]"
            >
              <img :src="movie.Poster" :alt="movie.Title" class="w-full h-full object-cover" />
            </div>
          </div>

          <!-- Content Container -->
          <div class="relative px-4 mt-4">
            <div class="pt-2">
              <h1 class="text-lg font-bold leading-tight">
                Guardians of the Galaxy Vol. 2
                <span class="text-white/60">(2017)</span>
              </h1>

              <div class="flex items-center gap-6 mt-6">
                <div class="flex items-center gap-3">
                  <!-- Score Circle -->
                  <div class="relative w-[40px] h-[40px]">
                    <div
                      class="absolute inset-0 rounded-full bg-[#081c22] flex items-center justify-center"
                    >
                      <div class="text-center">
                        <span class="text-[12px] font-bold">76</span>
                        <span class="text-[10px] align-super">%</span>
                      </div>
                    </div>
                    <svg class="absolute inset-0" viewBox="0 0 36 36">
                      <path
                        d="M18 2.0845
              a 15.9155 15.9155 0 0 1 0 31.831
              a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none"
                        stroke="#21d07a"
                        stroke-width="3"
                        stroke-dasharray="75, 100"
                      />
                    </svg>
                  </div>
                  <span class="text-md font-medium">User Score</span>
                </div>

                <!-- Vertical Divider -->
                <div class="h-8 w-px bg-white/20"></div>

                <!-- Play Trailer Button -->
                <button class="flex items-center gap-2 text-md font-medium">
                  <PlayIcon class="w-4 h-4" />
                  Play Trailer
                </button>
              </div>

              <div class="px-4 mt-6">
                <div class="flex items-center justify-center gap-2 font-medium text-md">
                  <span
                    class="inline-flex px-2 py-0.5 text-sm border border-white/30 rounded-[3px] font-bold bg-[#032541]/20"
                  >
                    12
                  </span>
                  <span class="text-white/90">{{ movie.Released }} (KR)</span>
                  <span class="text-white/90">•</span>
                  <span class="text-white/90">{{ movie.Runtime }}</span>
                </div>

                <!-- Genres -->
                <div class="mt-1 text-md text-white/90 font-medium tracking-wide text-center">
                  {{ movie.Genre }}
                </div>
              </div>

              <p class="mt-6 text-white/60 italic">Obviously.</p>

              <div class="mt-1">
                <h2 class="text-xl font-bold">Overview</h2>
                <p class="mt-2">{{ movie.Plot }}</p>
              </div>

              <div class="mt-8 grid grid-cols-2 gap-8 pb-16">
                <div v-for="member in crew" :key="member.name" class="flex flex-col">
                  <span class="font-bold">{{ member.name }}</span>
                  <span class="text-sm text-white/60">{{ member.role }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mobile Bottom Navigation -->
        <div class="fixed bottom-0 left-0 right-0 bg-[#032541] py-3">
          <div class="flex justify-around">
            <button>
              <ListBulletIcon class="w-6 h-6" />
            </button>
            <button>
              <HeartIcon class="w-6 h-6" />
            </button>
            <button>
              <BookmarkIcon class="w-6 h-6" />
            </button>
            <button>
              <StarIcon class="w-6 h-6" />
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
