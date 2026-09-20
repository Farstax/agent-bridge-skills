---
name: quick-tunnel
description: Use when a local HTTP service needs a temporary public URL for preview, webhook, browser, integration, or remote testing.
---

# Quick tunnel

Use this Skill to temporarily expose a local HTTP service through a Cloudflare Quick Tunnel.

Quick Tunnels are for development and testing only. They create a random public `*.trycloudflare.com` URL and proxy it to a local service through an outbound `cloudflared` connection. Do not use them as production ingress or as a substitute for the application's normal deployment path.

## Decide whether a tunnel is appropriate

Use a Quick Tunnel when the task requires a real public endpoint for something currently available only on localhost, such as:

- sharing a development preview;
- testing a webhook or callback;
- exercising an application from a remote browser or device;
- allowing an external test or evaluation harness to reach a local service;
- giving a human a temporary URL for reviewing running work.

Do not create a tunnel merely because a local server exists.

Starting a tunnel makes the selected local service publicly reachable. Only do so when the user has explicitly asked to expose or share it, or when the approved task clearly requires a public endpoint.

Do not expose services containing credentials, unrestricted administrative functions, sensitive customer data, private infrastructure controls, or other content that should not be publicly reachable.

## Verify the origin first

Identify the exact local URL that needs to be exposed.

Confirm that it responds locally before creating the tunnel. For example:

```bash
curl --fail --silent --show-error http://localhost:8000/
```

Do not work around a broken local service by creating a tunnel. Fix or report the local failure first.

## Start the tunnel

Require `cloudflared` to be available locally.

Expose the exact local URL:

```bash
cloudflared tunnel --url http://localhost:8000
```

Do not log in to Cloudflare, create DNS records, create named tunnels, or modify persistent Cloudflare configuration for this workflow.

Prefer machine-readable Quick Tunnel output when the installed `cloudflared` version explicitly supports it. Do not assume an undocumented output flag or schema; inspect the installed CLI when necessary.

Capture the generated HTTPS `*.trycloudflare.com` URL.

Keep the `cloudflared` process associated with the active work rather than installing it as a daemon or system service.

## Verify the public endpoint

A tunnel being created does not prove that the application works through it.

Request the public URL and verify the expected application response:

```bash
curl --fail --silent --show-error https://<generated-host>.trycloudflare.com/
```

For a webhook, browser flow, API, or other task-specific endpoint, exercise the actual path needed by the task rather than relying only on `/`.

A newly created hostname can take a short time before its first successful request. Retry briefly when the tunnel is running but the hostname has not become reachable yet.

## Use the tunnel

Return the public URL to the caller or use it for the approved test.

Treat the URL as public. Anyone who knows it can attempt to access the exposed service.

Remember the Quick Tunnel constraints:

- the hostname is temporary and changes when recreated;
- there is no uptime guarantee;
- it is intended for development and testing;
- Quick Tunnels are limited to 200 concurrent in-flight requests;
- Server-Sent Events are not supported.

If the task requires stable addressing, authentication at the tunnel boundary, production availability, or unsupported transport behaviour, stop using this Skill and use the project's normal deployment or ingress mechanism instead.

## Clean up

When the public endpoint is no longer required, terminate the `cloudflared` process.

Do not leave temporary tunnels running after the task that required them has completed.

No Cloudflare-side resource cleanup should be necessary for a Quick Tunnel because the tunnel exists only for the lifetime of the process.

## Completion

The task is complete when:

1. the intended local service was verified before exposure;
2. the Quick Tunnel was created successfully;
3. the generated public URL was verified from the public side;
4. the URL was used or returned for the requested purpose;
5. the temporary tunnel was terminated when no longer required.

Report the public URL while it is active and any limitation that materially affects the requested test.
