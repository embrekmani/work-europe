<template>
    <div class="navigation">
        <a href="/"><h1>Work Europe</h1></a>
        <a href="/post"><el-button type="primary">Post a job</el-button></a>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.navigation {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 1rem 1.5rem 1rem 1.5rem;
    a {
        text-decoration: none;
        color: #333;
        display: flex;
        align-items: center;
    }
    h1 {
        margin: 0;
    }
}
</style>
