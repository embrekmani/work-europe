<template>
  <el-container class="outer">
    <div class="title">Post a job for free</div>
    <div class="errors">
      <el-alert v-for="error in errors" :key="error" :title="error" type="error"/>
    </div>
    <el-form label-position="top" label-width="200px">
      <el-form-item label="Job Title">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="Location">
        <el-input v-model="form.location" placeholder="e.g. 'London', 'Berlin', 'Remote', etc."></el-input>
      </el-form-item>
      <el-form-item label="Company Name">
        <el-input v-model="form.company"></el-input>
      </el-form-item>
      <el-form-item label="Application Link">
        <el-input v-model="form.applicationLink" placeholder="e.g. 'https://www.company.com/apply' or 'apply@company.com'"></el-input>
      </el-form-item>
      <el-form-item label="Language(s)">
        <el-select
          v-model="form.languages"
          multiple
          placeholder="Language(s)">
          <el-option
            v-for="language in $store.state.languages"
            :key="language"
            :label="language"
            :value="language">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Job Description">
        <el-input v-model="form.description" type="textarea" rows="4" placeholder="You may use Markdown."></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="checkForm" type="primary">Post</el-button>
      </el-form-item>
    </el-form>
  </el-container>
</template>

<script>
import db from '~/server/firebaseInit'

export default {
  data() {
    return {
      form: {
        title: '',
        location: '',
        company: '',
        applicationLink: '',
        languages: [],
        description: '',
      },
      errors: [],
    }
  },
  methods: {
    checkForm() {
      this.errors = [];

      if (this.form.title == '' || this.form.location == '' || this.form.company == '' || this.form.applicationLink == '' || this.form.languages.length == 0 || this.form.description == '') {
        this.errors.push('All fields required.')
      }
      else if (this.form.title.length > 140) {
        this.errors.push('Title cannot exceed 140 characters.')
      }
      else if (this.form.location.length > 140) {
        this.errors.push('Location cannot exceed 140 characters.')
      }
      else if (this.form.company.length > 140) {
        this.errors.push('Company name cannot exceed 140 characters.')
      }
      else if (this.form.applicationLink.length > 1000) {
        this.errors.push('Application link cannot exceed 140 characters.')
      }
      else if (this.form.description.length > 10000) {
        this.errors.push('Description cannot exceed 10000 characters.')
      }
      else {
        db.collection('jobs').add({
          title: this.form.title,
          location: this.form.location,
          company: this.form.company,
          applicationLink: this.form.applicationLink,
          languages: this.form.languages,
          description: this.form.description,
        })
        .then(docRef => window.location = '/')
        .catch(error => console.log(error))
      }

      if (this.errors) {
        window.scrollTo(0, 0);
      }
    },
  },
}
</script>

<style lang="scss" scoped>

.el-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  .title {
    font-weight: 300;
    font-size: 2.5rem;
    color: #303133;
    margin-bottom: 1.5rem;
  }
}

.el-form {
  padding: 1rem;
  width: 80%;
  .el-select {
    width: 100%;
  }
  .el-button {
    float: right;
    min-width: 8rem;
    font-size: 1.25rem;
  }
}

.errors {
  width: 80%;
  .el-alert {
    margin-bottom: .75rem;
  }
}

@media (max-width: 769px) { 
  .el-form .el-button {
    width: 100%;
  }
}

</style>