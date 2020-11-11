<template>
    <ul>
        <li>
            <router-link
                :to="{
                    name: 'home'
                }"
            >
                Home
            </router-link>
        </li>
        <template v-if="authenticated">
            <li>
                {{ user.username }}
            </li>
            <li>
                <router-link
                    :to="{
                        name: 'dashboard'
                    }"
                >
                    Dashboard
                </router-link>
            </li>
            <li>
                <a href="#">
                    Sign out
                </a>
            </li>
        </template>
        <template v-else>
            <li>
                <router-link
                    :to="{
                        name: 'signin'
                    }"
                >
                    Sign in
                </router-link>
            </li>
        </template>
    </ul>
</template>

<script>
    import { mapGetters } from 'vuex'

    export default {
        computed: {
            ...mapGetters({
                authenticated: 'auth/authenticated',
                user: 'auth/user',
            })
        },
    }
</script>