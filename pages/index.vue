<template>
<div>
  <el-container class="outer">
    <el-aside width="400px">
      <h1>Find your place in Europe.</h1>
      <p>Work Europe is the job board for location agnostic EU tech workers. Just filter by your preferred language(s) and enjoy the freedom Europe has to offer!</p>
      <p>Made by Embrek Máni with ❤️</p>
      <p>Contact: <a href="mailto:embrekmani@gmail.com">embrekmani@gmail.com</a></p>
    </el-aside>

    <el-main>
      <el-carousel height="50vh" trigger="click">
        <el-carousel-item v-for="(img, i) in images" :key="i">
          <el-image :src="getImageUrl(img)" fit="contain"/>
        </el-carousel-item>
      </el-carousel>
    </el-main>
  </el-container>
  <el-container class="outer main">
    <div class="search">
      <el-select
        slot="prepend"
        v-model="selectedLanguages"
        multiple
        collapse-tags
        placeholder="Language(s)">
        <el-option
          v-for="language in $store.state.languages"
          :key="language"
          :label="language"
          :value="language">
        </el-option>
      </el-select>
      <el-input placeholder="Search..." v-on:keyup.enter="applyFilters" v-model="search" />
      <el-button @click="applyFilters" type="primary">Apply</el-button>
    </div>
    <div v-if="loadedJobs.length != 0" class="jobs">
      <Job v-for="job in loadedJobs" :key="job.id" :title="job.title" applicationLink="/apply" :company="job.company" :location="job.location" :languages="job.languages" :description="job.description" />
      <el-button v-if="loadedJobs.length < filteredJobs.length" class="load-button" @click="loadJobs" type="primary">Load more</el-button>
    </div>
    <div v-else class="no-jobs">
      <p>Sorry, no jobs found.</p>
    </div>
  </el-container>
</div>
</template>

<script>
import axios from 'axios';
import Job from '~/components/Job.vue';

export default {
  components: {
    Job
  },
  data() {
    return {
      jobs: [],
      filteredJobs: [],
      loadIndex: 1, // inital 25 already loaded, first load call must be 2 * 25 
      loadedJobs: [],
      selectedLanguages: [],
      search: '',
      images: ['benjamin-davies-Oja2ty_9ZLM-unsplash.jpg', 'chris-karidis-nnzkZNYWHaU-unsplash.jpg', 'stefan-widua-iPOZf3tQfHA-unsplash.jpg']
    }
  },
  methods: {
    getImageUrl(url) {
      return require('../static/' + url)
    },
    applyFilters(e) {
      e.preventDefault();
      let jobs = [];
      // if selected any languages, search after filter
      // else search
      if (this.selectedLanguages.length > 0) {
        this.jobs.forEach(job => {
          job.languages.forEach(language => {
            console.log(job)
            if (this.selectedLanguages.indexOf(language) > -1) {
              jobs.push(job);
            }
          })
        });
        if (this.search != '') {
          jobs = this.searchJobs(jobs);
        }
        this.filteredJobs = jobs;
      }
      else {
        if (this.search != '') {
          this.filteredJobs = this.searchJobs(this.jobs)
        }
        else {
          this.filteredJobs = this.jobs
        }
      }
    },
    searchJobs(jobs) {
      let result = [];
      jobs.forEach(job => {
        let search = this.search.toUpperCase().split(' ');
        search.forEach(searchTerm => {
          if (job.title.toUpperCase().indexOf(searchTerm) > -1 && result.indexOf(job) == -1) {
            result.push(job);
          }
        });
      });
      return result;
    },
    loadJobs() {
      this.loadIndex++;
      this.loadedJobs = this.filteredJobs.slice(0, this.loadIndex * 10)
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/jobs/').then(response => (this.jobs = response.data, this.filteredJobs = response.data, this.loadedJobs = response.data.slice(0, 25)));
  }
}
</script>

<style lang="scss">
.el-aside {
  padding: 1rem;
  h1 {
    margin: 0;
    font-weight: 300;
    font-size: 2.5rem;
    color: #303133;
  }
  p {
    color: #606266;
  }
}

.outer.main {
  flex-direction: row;
}

.el-carousel {
  width: 100%;
  border-radius: .25rem;
}

.search {
  min-width: 250px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  .el-select {
    width: 100%;
    .el-select__tags {
      top: 36%;
    }
  }
  .el-input {
    margin-bottom: 1rem;
  }
}

.jobs {
  padding: 1rem;
  width: 100%;
  .job {
    margin-bottom: 1rem;
    .link {
      z-index: 999;
      transition: all .3s ease;
      opacity: 0;
    }
    &:hover {
      .link {
        opacity: 1;
      }
    }
  }
  .el-button.load-button {
    display: block;
    margin: 2rem auto 1rem auto;
    width: 12rem;
  }
}
.no-jobs {
  color: #606266;
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

@media (max-width: 769px) { 
  .el-container {
    main {
      display: none;
    }
  }
  .el-container.outer.main {
    flex-direction: column;
    .jobs {
      width: auto;
    }
  }
  .el-aside {
    width: 100% !important;
  }
}

</style>
