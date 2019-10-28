<template>
    <el-card class="job" :class="{ open: isOpen }" shadow="hover">
        <div class="card-header" @click="open" slot="header">
            <div class="text">
                <span class="title">{{ title }}</span>
                <span class="subtitle">{{ company }}, <strong>{{ location }}</strong></span>
            </div>
            <a class="link" @mouseenter="canOpen = false" @mouseleave="canOpen = true" target="__blank" :href="applicationLink"><el-button type="text">Apply</el-button></a>
        </div>
        <div class="card-body">
            <!--<div v-html="compiledMarkdown"></div>-->
        </div>
    </el-card>
</template>

<script>

import marked from 'marked';
import lodash from 'lodash';

export default {
    props: {
        title: String,
        company: String,
        applicationLink: String,
        location: String,
        languages: Array,
        description: String,
    },
    data() {
        return {
            canOpen: true,
            isOpen: false,
        }
    },
    computed: {
        compiledMarkdown: function () {
            return marked(this.description)
        },
    },
    methods: {
        open() {
            if (this.canOpen) {
                this.isOpen = !this.isOpen;
            }
        }
    }
}
</script>

<style lang="scss">

.card-header {
    display: flex;
    justify-content: space-between;
    padding: 0 .5rem 0 0;
    align-items: center;
    font-size: 1.3rem;
    cursor: pointer;
    .text {
        display: flex;
        flex-direction: column;
        .title {
            transition: color .3s ease;
        }
        .subtitle {
            font-size: 1rem;
        }
    }
    .el-button {
        font-size: 1.25rem;
    }
    &:hover {
        .text {
            .title {
                color: #66b1ff;
            }
        }
    }
}

.job {
    .el-card__body {
        padding-top: 0;
        padding-bottom: 0;
        transition: all .3s ease;
        transform: scaleY(0);
        transform-origin: top;
        .card-body {
            transition: all .3s ease;
            font-size: 0;
            transform: scaleY(0);
            transform-origin: top;
            opacity: 0;
            span {
                opacity: 0;
                transition: opacity .3s ease;
                transition-delay: .3s;
            }
        }
    }
    &.open {
        .el-card__body {
            padding: 0 20px 0 20px;
            transform: scaleY(1);
            .card-body {
                transform: scaleY(1);
                font-size: inherit;
                opacity: 1;
                span {
                    opacity: 1;
                }
            }
        }
    }
}

</style>
